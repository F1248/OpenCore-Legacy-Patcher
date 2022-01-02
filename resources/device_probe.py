# Hardware probing
# Copyright (C) 2020-2022, Dhinak G, Mykola Grymalyuk

from __future__ import annotations

import binascii
import enum
import itertools
import subprocess
import plistlib
from dataclasses import dataclass, field
from typing import Any, ClassVar, Optional, Type, Union

from resources import utilities, ioreg
from data import pci_data


@dataclass
class CPU:
    name: str
    flags: list[str]


@dataclass
class PCIDevice:
    VENDOR_ID: ClassVar[int]  # Default vendor id, for subclasses.

    vendor_id: int  # The vendor ID of this PCI device
    device_id: int  # The device ID of this PCI device
    class_code: int  # The class code of this PCI device - https://pci-ids.ucw.cz/read/PD

    # ioregistryentry: Optional[ioreg.IORegistryEntry] = None
    name: Optional[str] = None  # Name of IORegistryEntry
    model: Optional[str] = None  # model property
    acpi_path: Optional[str] = None
    pci_path: Optional[str] = None

    # def __getstate__(self):
    #     state = self.__dict__.copy()
    #     state.pop("ioregistryentry")
    #     return state

    @classmethod
    def from_ioregistry(cls, entry: ioreg.io_registry_entry_t, anti_spoof=False):
        properties: dict = ioreg.corefoundation_to_native(ioreg.IORegistryEntryCreateCFProperties(entry, None, ioreg.kCFAllocatorDefault, ioreg.kNilOptions)[1])  # type: ignore
        if anti_spoof and "IOName" in properties:
            vendor_id, device_id = (int(i, 16) for i in properties["IOName"][3:].split(","))
        else:
            vendor_id, device_id = [int.from_bytes(properties[i][:4], byteorder="little") for i in ["vendor-id", "device-id"]]

        device = cls(vendor_id, device_id, int.from_bytes(properties["class-code"][:6], byteorder="little"), name=ioreg.io_name_t_to_str(ioreg.IORegistryEntryGetName(entry, None)[1]))
        if "model" in properties:
            device.model = properties["model"].strip(b"\0").decode()
        if "acpi-path" in properties:
            device.acpi_path = properties["acpi-path"]
        device.populate_pci_path(entry)
        return device

    # @staticmethod
    # def vendor_detect_old(device):
    #     for i in [NVIDIA, AMD]:
    #         if i.detect(device):
    #             return i
    #     return None

    def vendor_detect(self, *, inherits: ClassVar[Any] = None, classes: list = None):
        for i in classes or itertools.chain.from_iterable([subclass.__subclasses__() for subclass in PCIDevice.__subclasses__()]):
            if issubclass(i, inherits or object) and i.detect(self):
                return i
        return None

    @classmethod
    def detect(cls, device):
        return device.vendor_id == cls.VENDOR_ID and ((device.class_code == cls.CLASS_CODE) if getattr(cls, "CLASS_CODE", None) else True)  # type: ignore  # pylint: disable=no-member

    # def acpi_path(self):
    #     # Eventually
    #     raise NotImplementedError

    def populate_pci_path(self, original_entry: ioreg.io_registry_entry_t):
        # Based off gfxutil logic, seems to work.
        paths = []
        entry = original_entry
        while entry:
            if ioreg.IOObjectConformsTo(entry, "IOPCIDevice".encode()):
                location = [hex(int(i, 16)) for i in ioreg.io_name_t_to_str(ioreg.IORegistryEntryGetLocationInPlane(entry, "IOService".encode(), None)[1]).split(",") + ["0"]]
                paths.append(f"Pci({location[0]},{location[1]})")
            elif ioreg.IOObjectConformsTo(entry, "IOACPIPlatformDevice".encode()):
                paths.append(f"PciRoot({hex(int(ioreg.corefoundation_to_native(ioreg.IORegistryEntryCreateCFProperty(entry, '_UID', ioreg.kCFAllocatorDefault, ioreg.kNilOptions)) or 0))})")  # type: ignore
                break
            elif ioreg.IOObjectConformsTo(entry, "IOPCIBridge".encode()):
                pass
            else:
                # There's something in between that's not PCI! Abort
                paths = []
                break
            parent = ioreg.IORegistryEntryGetParentEntry(entry, "IOService".encode(), None)[1]
            if entry != original_entry:
                ioreg.IOObjectRelease(entry)
            entry = parent
        self.pci_path = "/".join(reversed(paths))


@dataclass
class GPU(PCIDevice):
    arch: enum.Enum = field(init=False)  # The architecture, see subclasses.

    def __post_init__(self):
        self.detect_arch()

    def detect_arch(self):
        raise NotImplementedError


@dataclass
class WirelessCard(PCIDevice):
    CLASS_CODE: ClassVar[int] = 0x028000  # 00800200 hexswapped
    country_code: str = field(init=False)
    chipset: enum.Enum = field(init=False)

    def __post_init__(self):
        self.detect_chipset()

    @classmethod
    def from_ioregistry(cls, entry: ioreg.io_registry_entry_t, anti_spoof=True):
        device = super().from_ioregistry(entry, anti_spoof=anti_spoof)

        matching_dict = {
            "IOParentMatch": ioreg.corefoundation_to_native(ioreg.IORegistryEntryIDMatching(ioreg.IORegistryEntryGetRegistryEntryID(entry, None)[1])),
            "IOProviderClass": "IO80211Interface",
        }

        interface = next(ioreg.ioiterator_to_list(ioreg.IOServiceGetMatchingServices(ioreg.kIOMasterPortDefault, matching_dict, None)[1]), None)
        if interface:
            device.country_code = ioreg.corefoundation_to_native(ioreg.IORegistryEntryCreateCFProperty(interface, "IO80211CountryCode", ioreg.kCFAllocatorDefault, ioreg.kNilOptions))  # type: ignore # If not present, will be None anyways
        else:
            device.country_code = None  # type: ignore

        return device

    def detect_chipset(self):
        raise NotImplementedError


@dataclass
class NVMeController(PCIDevice):
    CLASS_CODE: ClassVar[int] = 0x010802

    aspm: Optional[int] = None
    # parent_aspm: Optional[int] = None


@dataclass
class SATAController(PCIDevice):
    CLASS_CODE: ClassVar[int] = 0x010601

@dataclass
class SASController(PCIDevice):
    CLASS_CODE: ClassVar[int] = 0x010400


@dataclass
class NVIDIA(GPU):
    VENDOR_ID: ClassVar[int] = 0x10DE

    class Archs(enum.Enum):
        # pylint: disable=invalid-name
        Curie = "Curie"
        Fermi = "Fermi"
        Tesla = "Tesla"
        Kepler = "Kepler"
        Unknown = "Unknown"

    arch: Archs = field(init=False)

    def detect_arch(self):
        # G80/G80GL
        if self.device_id in pci_data.nvidia_ids.curie_ids:
            self.arch = NVIDIA.Archs.Curie
        elif self.device_id in pci_data.nvidia_ids.tesla_ids:
            self.arch = NVIDIA.Archs.Tesla
        elif self.device_id in pci_data.nvidia_ids.fermi_ids:
            self.arch = NVIDIA.Archs.Fermi
        elif self.device_id in pci_data.nvidia_ids.kepler_ids:
            self.arch = NVIDIA.Archs.Kepler
        else:
            self.arch = NVIDIA.Archs.Unknown


@dataclass
class AMD(GPU):
    VENDOR_ID: ClassVar[int] = 0x1002

    class Archs(enum.Enum):
        # pylint: disable=invalid-name
        R500 = "R500"
        TeraScale_1 = "TeraScale 1"
        TeraScale_2 = "TeraScale 2"
        Legacy_GCN_7000 = "Legacy GCN v1"
        Legacy_GCN_8000 = "Legacy GCN v2"
        Legacy_GCN_9000 = "Legacy GCN v3"
        Polaris = "Polaris"
        Vega = "Vega"
        Navi = "Navi"
        Unknown = "Unknown"

    arch: Archs = field(init=False)

    def detect_arch(self):
        if self.device_id in pci_data.amd_ids.r500_ids:
            self.arch = AMD.Archs.R500
        elif self.device_id in pci_data.amd_ids.gcn_7000_ids:
            self.arch = AMD.Archs.Legacy_GCN_7000
        elif self.device_id in pci_data.amd_ids.gcn_8000_ids:
            self.arch = AMD.Archs.Legacy_GCN_8000
        elif self.device_id in pci_data.amd_ids.gcn_9000_ids:
            self.arch = AMD.Archs.Legacy_GCN_9000
        elif self.device_id in pci_data.amd_ids.terascale_1_ids:
            self.arch = AMD.Archs.TeraScale_1
        elif self.device_id in pci_data.amd_ids.terascale_2_ids:
            self.arch = AMD.Archs.TeraScale_2
        elif self.device_id in pci_data.amd_ids.polaris_ids:
            self.arch = AMD.Archs.Polaris
        elif self.device_id in pci_data.amd_ids.vega_ids:
            self.arch = AMD.Archs.Vega
        elif self.device_id in pci_data.amd_ids.navi_ids:
            self.arch = AMD.Archs.Navi
        else:
            self.arch = AMD.Archs.Unknown


@dataclass
class Intel(GPU):
    VENDOR_ID: ClassVar[int] = 0x8086

    class Archs(enum.Enum):
        # pylint: disable=invalid-name
        GMA_950 = "GMA 950"
        GMA_X3100 = "GMA X3100"
        Iron_Lake = "Iron Lake"
        Sandy_Bridge = "Sandy Bridge"
        Ivy_Bridge = "Ivy Bridge"
        Haswell = "Haswell"
        Broadwell = "Broadwell"
        Skylake = "Skylake"
        Kaby_Lake = "Kaby Lake"
        Coffee_Lake = "Coffee Lake"
        Comet_Lake = "Comet Lake"
        Ice_Lake = "Ice Lake"
        Unknown = "Unknown"

    arch: Archs = field(init=False)

    def detect_arch(self):
        if self.device_id in pci_data.intel_ids.gma_950_ids:
            self.arch = Intel.Archs.GMA_950
        elif self.device_id in pci_data.intel_ids.gma_x3100_ids:
            self.arch = Intel.Archs.GMA_X3100
        elif self.device_id in pci_data.intel_ids.iron_ids:
            self.arch = Intel.Archs.Iron_Lake
        elif self.device_id in pci_data.intel_ids.sandy_ids:
            self.arch = Intel.Archs.Sandy_Bridge
        elif self.device_id in pci_data.intel_ids.ivy_ids:
            self.arch = Intel.Archs.Ivy_Bridge
        elif self.device_id in pci_data.intel_ids.haswell_ids:
            self.arch = Intel.Archs.Haswell
        elif self.device_id in pci_data.intel_ids.broadwell_ids:
            self.arch = Intel.Archs.Broadwell
        elif self.device_id in pci_data.intel_ids.skylake_ids:
            self.arch = Intel.Archs.Skylake
        elif self.device_id in pci_data.intel_ids.kaby_lake_ids:
            self.arch = Intel.Archs.Kaby_Lake
        elif self.device_id in pci_data.intel_ids.coffee_lake_ids:
            self.arch = Intel.Archs.Coffee_Lake
        elif self.device_id in pci_data.intel_ids.comet_lake_ids:
            self.arch = Intel.Archs.Comet_Lake
        elif self.device_id in pci_data.intel_ids.ice_lake_ids:
            self.arch = Intel.Archs.Ice_Lake
        else:
            self.arch = Intel.Archs.Unknown


@dataclass
class Broadcom(WirelessCard):
    VENDOR_ID: ClassVar[int] = 0x14E4

    class Chipsets(enum.Enum):
        # pylint: disable=invalid-name
        AppleBCMWLANBusInterfacePCIe = "AppleBCMWLANBusInterfacePCIe supported"
        AirportBrcmNIC = "AirportBrcmNIC supported"
        AirPortBrcm4360 = "AirPortBrcm4360 supported"
        AirPortBrcm4331 = "AirPortBrcm4331 supported"
        AirPortBrcm43224 = "AppleAirPortBrcm43224 supported"
        Unknown = "Unknown"

    chipset: Chipsets = field(init=False)

    def detect_chipset(self):
        if self.device_id in pci_data.broadcom_ids.AppleBCMWLANBusInterfacePCIe:
            self.chipset = Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe
        elif self.device_id in pci_data.broadcom_ids.AirPortBrcmNIC:
            self.chipset = Broadcom.Chipsets.AirportBrcmNIC
        elif self.device_id in pci_data.broadcom_ids.AirPortBrcm4360:
            self.chipset = Broadcom.Chipsets.AirPortBrcm4360
        elif self.device_id in pci_data.broadcom_ids.AirPortBrcm4331:
            self.chipset = Broadcom.Chipsets.AirPortBrcm4331
        elif self.device_id in pci_data.broadcom_ids.AppleAirPortBrcm43224:
            self.chipset = Broadcom.Chipsets.AirPortBrcm43224
        else:
            self.chipset = Broadcom.Chipsets.Unknown


@dataclass
class Atheros(WirelessCard):
    VENDOR_ID: ClassVar[int] = 0x168C

    class Chipsets(enum.Enum):
        # pylint: disable=invalid-name
        # Well there's only one model but
        AirPortAtheros40 = "AirPortAtheros40 supported"
        Unknown = "Unknown"

    chipset: Chipsets = field(init=False)

    def detect_chipset(self):
        if self.device_id in pci_data.atheros_ids.AtherosWifi:
            self.chipset = Atheros.Chipsets.AirPortAtheros40
        else:
            self.chipset = Atheros.Chipsets.Unknown


@dataclass
class Computer:
    real_model: Optional[str] = None
    real_board_id: Optional[str] = None
    reported_model: Optional[str] = None
    reported_board_id: Optional[str] = None
    gpus: list[GPU] = field(default_factory=list)
    igpu: Optional[GPU] = None  # Shortcut for IGPU
    dgpu: Optional[GPU] = None  # Shortcut for GFX0
    storage: list[PCIDevice] = field(default_factory=list)
    wifi: Optional[WirelessCard] = None
    cpu: Optional[CPU] = None
    oclp_version: Optional[str] = None
    opencore_version: Optional[str] = None
    bluetooth_chipset: Optional[str] = None
    third_party_sata_ssd: Optional[bool] = False

    @staticmethod
    def probe():
        computer = Computer()
        computer.gpu_probe()
        computer.dgpu_probe()
        computer.igpu_probe()
        computer.wifi_probe()
        computer.storage_probe()
        computer.smbios_probe()
        computer.cpu_probe()
        computer.bluetooth_probe()
        computer.sata_disk_probe()
        return computer

    def gpu_probe(self):
        # Chain together two iterators: one for class code 00000300, the other for class code 00800300
        devices = ioreg.ioiterator_to_list(
            ioreg.IOServiceGetMatchingServices(
                ioreg.kIOMasterPortDefault, {"IOProviderClass": "IOPCIDevice", "IOPropertyMatch": [{"class-code": binascii.a2b_hex("00000300")}, {"class-code": binascii.a2b_hex("00800300")}]}, None
            )[1]
        )

        for device in devices:
            vendor: Type[GPU] = PCIDevice.from_ioregistry(device).vendor_detect(inherits=GPU)  # type: ignore
            if vendor:
                self.gpus.append(vendor.from_ioregistry(device))  # type: ignore
            ioreg.IOObjectRelease(device)

    def dgpu_probe(self):
        device = next(ioreg.ioiterator_to_list(ioreg.IOServiceGetMatchingServices(ioreg.kIOMasterPortDefault, ioreg.IOServiceNameMatching("GFX0".encode()), None)[1]), None)
        if not device:
            # No devices
            return

        vendor: Type[GPU] = PCIDevice.from_ioregistry(device).vendor_detect(inherits=GPU)  # type: ignore
        if vendor:
            self.dgpu = vendor.from_ioregistry(device)  # type: ignore
        ioreg.IOObjectRelease(device)

    def igpu_probe(self):
        device = next(ioreg.ioiterator_to_list(ioreg.IOServiceGetMatchingServices(ioreg.kIOMasterPortDefault, ioreg.IOServiceNameMatching("IGPU".encode()), None)[1]), None)
        if not device:
            # No devices
            return

        vendor: Type[GPU] = PCIDevice.from_ioregistry(device).vendor_detect(inherits=GPU)  # type: ignore
        if vendor:
            self.igpu = vendor.from_ioregistry(device)  # type: ignore
        ioreg.IOObjectRelease(device)

    def wifi_probe(self):
        # result = subprocess.run("ioreg -r -c IOPCIDevice -a -d2".split(), stdout=subprocess.PIPE).stdout.strip()
        devices = ioreg.ioiterator_to_list(
            ioreg.IOServiceGetMatchingServices(
                ioreg.kIOMasterPortDefault,
                {"IOProviderClass": "IOPCIDevice", "IOPropertyMatch": {"class-code": binascii.a2b_hex(utilities.hexswap(hex(WirelessCard.CLASS_CODE)[2:].zfill(8)))}},
                None,
            )[1]
        )

        for device in devices:
            vendor: Type[WirelessCard] = PCIDevice.from_ioregistry(device, anti_spoof=True).vendor_detect(inherits=WirelessCard)  # type: ignore
            if vendor:
                self.wifi = vendor.from_ioregistry(device, anti_spoof=True)  # type: ignore
                break
            ioreg.IOObjectRelease(device)

    def storage_probe(self):
        sata_controllers = ioreg.ioiterator_to_list(
            ioreg.IOServiceGetMatchingServices(
                ioreg.kIOMasterPortDefault,
                {"IOProviderClass": "IOPCIDevice", "IOPropertyMatch": [{"class-code": binascii.a2b_hex(utilities.hexswap(hex(SATAController.CLASS_CODE)[2:].zfill(8)))}]},
                None,
            )[1]
        )
        sas_controllers = ioreg.ioiterator_to_list(
            ioreg.IOServiceGetMatchingServices(
                ioreg.kIOMasterPortDefault,
                {"IOProviderClass": "IOPCIDevice", "IOPropertyMatch": [{"class-code": binascii.a2b_hex(utilities.hexswap(hex(SASController.CLASS_CODE)[2:].zfill(8)))}]},
                None,
            )[1]
        )

        nvme_controllers = ioreg.ioiterator_to_list(
            ioreg.IOServiceGetMatchingServices(
                ioreg.kIOMasterPortDefault, {"IOProviderClass": "IONVMeController", "IOParentMatch": {"IOProviderClass": "IOPCIDevice"}, "IOPropertyMatch": {"IOClass": "IONVMeController"}}, None
            )[1]
        )
        for device in sata_controllers:
            self.storage.append(SATAController.from_ioregistry(device))
            ioreg.IOObjectRelease(device)
        
        for device in sas_controllers:
            self.storage.append(SASController.from_ioregistry(device))
            ioreg.IOObjectRelease(device)

        for device in nvme_controllers:
            parent = ioreg.IORegistryEntryGetParentEntry(device, "IOService".encode(), None)[1]
            ioreg.IOObjectRelease(device)

            aspm: Union[int, bytes] = ioreg.corefoundation_to_native(ioreg.IORegistryEntryCreateCFProperty(parent, "pci-aspm-default", ioreg.kCFAllocatorDefault, ioreg.kNilOptions)) or 0  # type: ignore
            if isinstance(aspm, bytes):
                aspm = int.from_bytes(aspm, byteorder="little")

            controller = NVMeController.from_ioregistry(parent)
            controller.aspm = aspm

            if controller.vendor_id != 0x106B:
                # Handle Apple Vendor ID
                self.storage.append(controller)

            ioreg.IOObjectRelease(parent)

    def smbios_probe(self):
        # Reported model
        entry = next(ioreg.ioiterator_to_list(ioreg.IOServiceGetMatchingServices(ioreg.kIOMasterPortDefault, ioreg.IOServiceMatching("IOPlatformExpertDevice".encode()), None)[1]))
        self.reported_model = ioreg.corefoundation_to_native(ioreg.IORegistryEntryCreateCFProperty(entry, "model", ioreg.kCFAllocatorDefault, ioreg.kNilOptions)).strip(b"\0").decode()  # type: ignore
        translated = subprocess.run("sysctl -in sysctl.proc_translated".split(), stdout=subprocess.PIPE).stdout.decode()
        if translated:
            board = "target-type"
        else:
            board = "board-id"
        self.reported_board_id = ioreg.corefoundation_to_native(ioreg.IORegistryEntryCreateCFProperty(entry, board, ioreg.kCFAllocatorDefault, ioreg.kNilOptions)).strip(b"\0").decode()  # type: ignore
        ioreg.IOObjectRelease(entry)

        # Real model
        # TODO: We previously had logic for OC users using iMacPro1,1 with incorrect ExposeSensitiveData. Add logic?
        self.real_model = utilities.get_nvram("oem-product", "4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102", decode=True) or self.reported_model
        self.real_board_id = utilities.get_nvram("oem-board", "4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102", decode=True) or self.reported_board_id

        # OCLP version
        self.oclp_version = utilities.get_nvram("OCLP-Version", "4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102", decode=True)
        self.opencore_version = utilities.get_nvram("opencore-version", "4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102", decode=True)

    def cpu_probe(self):
        self.cpu = CPU(
            subprocess.run("sysctl machdep.cpu.brand_string".split(), stdout=subprocess.PIPE).stdout.decode().partition(": ")[2].strip(),
            subprocess.run("sysctl machdep.cpu.features".split(), stdout=subprocess.PIPE).stdout.decode().partition(": ")[2].strip().split(" "),
        )

    def bluetooth_probe(self):
        usb_data: str = subprocess.run("system_profiler SPUSBDataType".split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()
        if "BRCM2070 Hub" in usb_data:
            self.bluetooth_chipset = "BRCM2070 Hub"
        elif "BRCM2046 Hub" in usb_data:
            self.bluetooth_chipset = "BRCM2046 Hub"
        elif "BRCM20702 Hub" in usb_data:
            self.bluetooth_chipset = "BRCM20702 Hub"
        elif "Bluetooth":
            self.bluetooth_chipset = "Generic"
    
    def sata_disk_probe(self):
        # Get all SATA Controllers/Disks from 'system_profiler SPSerialATADataType'
        # Determine whether SATA SSD is present and Apple-made
        sp_sata_data = plistlib.loads(subprocess.run(f"system_profiler SPSerialATADataType -xml".split(), stdout=subprocess.PIPE).stdout.decode().strip().encode())
        for root in sp_sata_data:
            for ahci_controller in root["_items"]:
                # Each AHCI controller will have its own entry
                # Skip entries that are AHCI PCIe controllers
                # Apple's AHCI PCIe controller will report 'PCI' interconnect
                try:
                    if ahci_controller["spsata_physical_interconnect"] == "SATA":
                        for port in ahci_controller["_items"]:
                            if port["spsata_medium_type"] == "Solid State" and "apple" not in port["device_model"].lower():
                                self.third_party_sata_ssd = True
                                # Bail out of loop as we only need to know if there are any third-party SSDs present
                                break
                except KeyError:
                    # Notes: 
                    # - SATA Optical Disk Drives don't report 'spsata_medium_type'
                    # - 'spsata_physical_interconnect' was not introduced till 10.9
                    continue
        
