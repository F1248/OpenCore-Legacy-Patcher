# Defines Model Data
# Terms:
#   AAPL: AppleInternal Model (ie. not released to public)
#   Board ID: The board ID is a unique identifier for the motherboard.
#   Firmware Features: Hex bitmask denoting supported abilities of firmware. (ie. APFS, Large BaseSystem, etc.)
#   Secure Boot Model: T2/Apple Silicon Model Identifier
#   CPU Generation: Stock CPU supported by the board (generally lowest generation)
#   Wireless Model: Driver used for wireless networking
#   Bluetooth Model: Chipset model
#   Screen Size: Size of the screen in inches (generally lowest size if multiple in same model)
#   UGA Graphics: If model needs UGA to GOP conversion
#   Ethernet Chipset: Vendor of the ethernet chipset (if multiple unique chipset within Vendor, chipset name is used)
#   nForce Chipset: If model uses nForce chipset
#   Switchable GPUs: If model uses a GMUX
#   Stock GPUs: GPUs variations shipped

from resources import device_probe
from data import cpu_data, os_data, bluetooth_data

smbios_dictionary = {
    "MacBook1,1": {
        "Board ID": "Mac-F4208CC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.yonah.value,
        "Max OS Supported": os_data.os_data.snow_leopard,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 13,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_950
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBook2,1": {
        "Board ID": "Mac-F4208CA9",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 13,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_950
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBook3,1": {
        "Board ID": "Mac-F22788C8",
        "FirmwareFeatures": "0xC0001407",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 13,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_X3100
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBook4,1": {
        "Board ID": "Mac-F22788A9",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_X3100
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBook5,1": {
        "Board ID": "Mac-F42D89C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBook5,1_v2": {
        "Board ID": "Mac-F42D89A9",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBook5,2": {
        "Board ID": "Mac-F22788AA",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "Ethernet Chipset": "Nvidia",
        "Legacy iSight": True,
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBook6,1": {
        "Board ID": "Mac-F22C8AC8",
        "FirmwareFeatures": "0xFC0FE13F",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 13,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBook7,1": {
        "Board ID": "Mac-F22C89C8",
        "FirmwareFeatures": "0xFC0FE13F",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 13,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBook8,1": {
        "Board ID": "Mac-BE0E8AC46FE800CC",
        "FirmwareFeatures": "0xFC0FE13F",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.broadwell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 12,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Broadwell
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBook8,1_v2": {
        "Board ID": "Mac-F305150B0C7DEEEF",
        "FirmwareFeatures": "0xFC0FE13F",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.broadwell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 12,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Broadwell
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBook9,1": {
        "Board ID": "Mac-9AE82516C7C6B903",
        "FirmwareFeatures": "0xFC0FE13F",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 12,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Skylake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBook10,1": {
        "Board ID": "Mac-EE2EBD4B90B839A8",
        "FirmwareFeatures": "0xFC0FE13F",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.kaby_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 12,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Kaby_Lake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir1,1": {
        "Board ID": "Mac-F42C8CC8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_X3100
        ],
        "Stock Storage": [
            "SATA 1.8",
        ],
    },
    "MacBookAir2,1": {
        "Board ID": "Mac-F42D88C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "nForce Chipset": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 1.8",
        ],
    },
    "MacBookAir3,1": {
        "Board ID": "Mac-942452F5819B1C1B",
        "FirmwareFeatures": "0xD00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 11,
        "nForce Chipset": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookAir3,2": {
        "Board ID": "Mac-942C5DF58193131B",
        "FirmwareFeatures": "0xD00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "nForce Chipset": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookAir4,1": {
        "Board ID": "Mac-C08A6BB70A942AC2",
        "FirmwareFeatures": "0xD00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 11,
        "Ethernet Chipset": "Broadcom",  # Set for Apple Thunderbolt Adapter
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookAir4,2": {
        "Board ID": "Mac-742912EFDBEE19B3",
        "FirmwareFeatures": "0xD00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 13,
        "Ethernet Chipset": "Broadcom",  # Set for Apple Thunderbolt Adapter
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookAir5,1": {
        "Board ID": "Mac-66F35F19FE2A0D05",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Screen Size": 11,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookAir5,2": {
        "Board ID": "Mac-2E6FAB96566FE58C",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookAir6,1": {
        "Board ID": "Mac-35C1E88140C3E6CF",
        "FirmwareFeatures": "0xE00FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 11,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookAir6,2": {
        "Board ID": "Mac-7DF21CB3ED6977E5",
        "FirmwareFeatures": "0xE00FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir7,1": {
        "Board ID": "Mac-9F18E312C5C2BF0B",
        "FirmwareFeatures": "0xFF0FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.broadwell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 11,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Broadwell
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir7,2": {
        "Board ID": "Mac-937CB26E2E02BB01",
        "FirmwareFeatures": "0xFF0FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.broadwell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Broadwell
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir8,1": {
        "Board ID": "Mac-827FAC58A8FDFA22",
        "FirmwareFeatures": "0xFD8FF42E",
        "SecureBootModel": "j140k",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir8,1_v2": {
        "Board ID": "Mac-112818653D3AABFC",
        "FirmwareFeatures": "0xFD8FF42E",
        "SecureBootModel": "j140k",  # TODO: Verify
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "AAPL_MacBookAir8,1": {
        # AppleInternal MacBookAir8,1
        # True Model unknown
        "Board ID": "Mac-827FAC58A8FDFA22",
        "FirmwareFeatures": "0xFD8FF42E",
        "SecureBootModel": "x589amlu",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir8,2": {
        "Board ID": "Mac-226CB3C6A851A671",
        "FirmwareFeatures": "0xFD8FF42E",
        "SecureBootModel": "j140a",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir9,1": {
        "Board ID": "Mac-0CFF9C7C2B63DF8D",
        "FirmwareFeatures": "0xFFAFF06E",
        "SecureBootModel": "j230k",
        "CPU Generation": cpu_data.cpu_data.ice_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Ice_Lake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "AAPL_MacBookAir9,1": {
        # AppleInternal MacBookAir9,1
        # True Model unknown
        "Board ID": "Mac-0CFF9C7C2B63DF8D",
        "FirmwareFeatures": "0xFFAFF06E",
        "SecureBootModel": "x589icly",
        "CPU Generation": cpu_data.cpu_data.ice_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Ice_Lake
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookAir10,1": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j313",
        "CPU Generation": cpu_data.cpu_data.apple_m1.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Ethernet Chipset": None,
        "Stock GPUs": [], # TODO: Add Apple Silicon GPU
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro1,1": {
        "Board ID": "Mac-F425BEC8",
        "FirmwareFeatures": "",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.yonah.value,
        "Max OS Supported": os_data.os_data.snow_leopard,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 15,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.R500
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro1,2": {
        "Board ID": "Mac-F42DBEC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.yonah.value,
        "Max OS Supported": os_data.os_data.snow_leopard,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 17,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.R500
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro2,1": {
        "Board ID": "Mac-F42189C8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 17,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.R500
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro2,2": {
        "Board ID": "Mac-F42187C8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 15,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.R500
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro3,1": {
        "Board ID": "Mac-F4238BC8",
        "FirmwareFeatures": "0xC0001407",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 15,  # Shipped with 17 as well
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro3,1_v2": {
        "Board ID": "Mac-F42388C8",
        "FirmwareFeatures": "0xC0001407",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Screen Size": 15,  # Shipped with 17 as well
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro4,1": {
        "Board ID": "Mac-F42C89C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 15,  # Shipped with 17 as well
        "Switchable GPUs": True,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro4,1_v2": {
        "Board ID": "Mac-F42C86C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 15,  # Shipped with 17 as well
        "Switchable GPUs": True,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "MacBookPro5,1": {
        "Board ID": "Mac-F42D86C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro5,1_v2": {
        "Board ID": "Mac-F42D86A9",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro5,2": {
        "Board ID": "Mac-F2268EC8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 17,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro5,3": {
        "Board ID": "Mac-F22587C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro5,4": {
        "Board ID": "Mac-F22587A1",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro5,5": {
        "Board ID": "Mac-F2268AC8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro6,1": {
        "Board ID": "Mac-F22589C8",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 17,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Iron_Lake,
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro6,2": {
        "Board ID": "Mac-F22586C8",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Iron_Lake,
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro7,1": {
        "Board ID": "Mac-F222BEC8",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Screen Size": 13,
        "Ethernet Chipset": "Broadcom",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro8,1": {
        "Board ID": "Mac-94245B3640C91C81",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 13,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro8,2": {
        "Board ID": "Mac-94245A3940C91C80",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro8,3": {
        "Board ID": "Mac-942459F5819B171B",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 17,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "AAPL_MacBookPro8,3": {
        # AppleInternal MacBookPro8,3
        # True Model unknown
        "Board ID": "Mac-94245AF5819B141B",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Screen Size": 17,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro9,1": {
        "Board ID": "Mac-4B7AC7E43945597E",
        "FirmwareFeatures": "0xC00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge,
            device_probe.NVIDIA.Archs.Kepler
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro9,2": {
        "Board ID": "Mac-6F01561E16C75D06",
        "FirmwareFeatures": "0xC10DF577",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Screen Size": 13,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Kepler
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "MacBookPro10,1": {
        "Board ID": "Mac-C3EC7CD22292981F",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge,
            device_probe.NVIDIA.Archs.Kepler
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookPro10,2": {
        "Board ID": "Mac-AFD8A9D944EA4843",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Kepler
        ],
        "Stock Storage": [
            "mSATA",
        ],
    },
    "MacBookPro11,1": {
        "Board ID": "Mac-189A3D4F975D5FFC",
        "FirmwareFeatures": "0xEB0FF577",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro11,2": {
        "Board ID": "Mac-3CBD00234E554E41",
        "FirmwareFeatures": "0xEB0FF577",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 15,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro11,3": {
        "Board ID": "Mac-2BD1B31983FE1663",
        "FirmwareFeatures": "0xEB0FF577",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro11,4": {
        "Board ID": "Mac-06F11FD93F0323C5",
        "FirmwareFeatures": "0xEB0FF577",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 15,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro11,5": {
        "Board ID": "Mac-06F11F11946D27C5",
        "FirmwareFeatures": "0xEB0FF577",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
            device_probe.AMD.Archs.Legacy_GCN_7000
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro12,1": {
        "Board ID": "Mac-E43C1C25D4880AD6",
        "FirmwareFeatures": "0xFD0FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.broadwell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Broadwell,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro13,1": {
        "Board ID": "Mac-473D31EABEB93F9B",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Skylake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro13,2": {
        "Board ID": "Mac-66E35819EE2D0D05",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Skylake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro13,3": {
        "Board ID": "Mac-A5C67F76ED83108C",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Skylake,
            device_probe.AMD.Archs.Polaris
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro14,1": {
        "Board ID": "Mac-B4831CEBD52A0C4C",
        "FirmwareFeatures": "0xFF0FF57E",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.kaby_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Kaby_Lake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro14,2": {
        "Board ID": "Mac-CAD6701F7CEA0921",
        "FirmwareFeatures": "0xFF0FF57E",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.kaby_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Kaby_Lake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro14,3": {
        "Board ID": "Mac-551B86E5744E2388",
        "FirmwareFeatures": "0xFF0FF57E",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.kaby_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703_UART,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Kaby_Lake,
            device_probe.AMD.Archs.Polaris
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro15,1": {
        "Board ID": "Mac-937A206F2EE63C01",
        "FirmwareFeatures": "0xFD8FF426",
        "SecureBootModel": "j680",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
            device_probe.AMD.Archs.Polaris
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro15,2": {
        "Board ID": "Mac-827FB448E656EC26",
        "FirmwareFeatures": "0xFD8FF426",
        "SecureBootModel": "j132",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro15,3": {
        "Board ID": "Mac-1E7E29AD0135F9BC",
        "FirmwareFeatures": "0xFD8FF426",
        "SecureBootModel": "j780",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 15,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
            device_probe.AMD.Archs.Vega
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro15,4": {
        "Board ID": "Mac-53FDB3D8DB8CA971",
        "FirmwareFeatures": "0xFD8FF426",
        "SecureBootModel": "j213",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro16,1": {
        "Board ID": "Mac-E1008331FDC96864",
        "FirmwareFeatures": "0xFDAFF066",
        "SecureBootModel": "j152f",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 16,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
            device_probe.AMD.Archs.Navi
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro16,2": {
        "Board ID": "Mac-5F9802EFE386AA28",
        "FirmwareFeatures": "0xFFAFF06E",
        "SecureBootModel": "j214k",
        "CPU Generation": cpu_data.cpu_data.ice_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Ice_Lake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro16,3": {
        "Board ID": "Mac-E7203C0F68AA0004",
        "FirmwareFeatures": "0xFDAFF066",
        "SecureBootModel": "j223",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro16,4": {
        "Board ID": "Mac-A61BADE1FDAD7B05",
        "FirmwareFeatures": "0xFDAFF066",
        "SecureBootModel": "j215",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Screen Size": 16,
        "Switchable GPUs": True,
        "Ethernet Chipset": None,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
            device_probe.AMD.Archs.Navi
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro17,1": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j293",
        "CPU Generation": cpu_data.cpu_data.apple_m1.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Screen Size": 13,
        "Ethernet Chipset": None,
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro18,1": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j316s",
        "CPU Generation": cpu_data.cpu_data.apple_m1_pro.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Screen Size": 16,
        "Ethernet Chipset": None,
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro18,2": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j316c",
        "CPU Generation": cpu_data.cpu_data.apple_m1_max.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Screen Size": 16,
        "Ethernet Chipset": None,
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro18,3": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j314s",
        "CPU Generation": cpu_data.cpu_data.apple_m1_pro.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Screen Size": 14,
        "Ethernet Chipset": None,
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacBookPro18,4": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j314c",
        "CPU Generation": cpu_data.cpu_data.apple_m1_max.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Screen Size": 14,
        "Ethernet Chipset": None,
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "Macmini1,1": {
        "Board ID": "Mac-F4208EC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.yonah.value,
        "Max OS Supported": os_data.os_data.snow_leopard,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_950
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "Macmini2,1": {
        "Board ID": "Mac-F4208EAA",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_950
        ],
        "Stock Storage": [
            "SATA 2.5",
            "PATA",
        ],
    },
    "Macmini3,1": {
        "Board ID": "Mac-F22C86C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "Macmini4,1": {
        "Board ID": "Mac-F2208EC8",
        "FirmwareFeatures": "0xC00C9423",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "Macmini5,1": {
        "Board ID": "Mac-8ED6AF5B48C039E1",
        "FirmwareFeatures": "0xD00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "Macmini5,2": {
        "Board ID": "Mac-4BC72D62AD45599E",
        "FirmwareFeatures": "0xD00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "Macmini5,3": {
        "Board ID": "Mac-7BA5B2794B2CDB12",
        "FirmwareFeatures": "0xD00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2070,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "Macmini6,1": {
        "Board ID": "Mac-031AEE4D24BFF0B1",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge,
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "Macmini6,2": {
        "Board ID": "Mac-F65AE981FFA204ED",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge,
        ],
        "Stock Storage": [
            "SATA 2.5",
        ],
    },
    "Macmini7,1": {
        "Board ID": "Mac-35C5E08120C7EEAF",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
        ],
        "Stock Storage": [
            "SATA 2.5",
            "NVMe",
        ],
    },
    "Macmini8,1": {
        "Board ID": "Mac-7BA5B2DFE22DDD8C",
        "FirmwareFeatures": "0xFD8FF466",
        "SecureBootModel": "j174",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "Macmini9,1": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j274",
        "CPU Generation": cpu_data.cpu_data.apple_m1.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "iMac4,1": {
        "Board ID": "Mac-F42786C8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.yonah.value,
        "Max OS Supported": os_data.os_data.snow_leopard,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.AMD.Archs.R500,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac4,2": {
        "Board ID": "Mac-F4218EC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.yonah.value,
        "Max OS Supported": os_data.os_data.snow_leopard,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_950,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac5,1": {
        "Board ID": "Mac-F4228EC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.AMD.Archs.R500,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac5,2": {
        "Board ID": "Mac-F4218EC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_950,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac6,1": {
        "Board ID": "Mac-F4218FC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Legacy iSight": True,
        "Stock GPUs": [
            device_probe.AMD.Archs.R500,
            device_probe.NVIDIA.Archs.Curie
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac7,1": {
        "Board ID": "Mac-F42386C8",
        "FirmwareFeatures": "0xC0001407",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn,  # Stock models shipped with Conroe
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1,
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac7,1_v2": {
        "Board ID": "Mac-F4238CC8",
        "FirmwareFeatures": "0xC0001407",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn,  # Stock models shipped with Conroe
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1,
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac8,1": {
        "Board ID": "Mac-F227BEC8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1,
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac8,1_v2": {
        "Board ID": "Mac-F226BEC8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "UGA Graphics": True,
        "Ethernet Chipset": "Marvell",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1,
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "iMac9,1": {
        "Board ID": "Mac-F2218FA9",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac9,1_v2": {
        "Board ID": "Mac-F2218EA9",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac9,1_v3": {
        "Board ID": "Mac-F2218EC8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac9,1_v4": {
        "Board ID": "Mac-F2218FC8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac10,1": {
        "Board ID": "Mac-F221DCC8",
        # "Board ID": "Mac-F2268CC8",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac10,1_v2": {
        "Board ID": "Mac-F2268CC8",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac10,1_v3": {
        "Board ID": "Mac-F2268DC8",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Nvidia",
        "nForce Chipset": True,
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac11,1": {
        "Board ID": "Mac-F2268DAE",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac11,2": {
        "Board ID": "Mac-F2238AC8",
        "FirmwareFeatures": "0xC00C9423",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1,
            device_probe.AMD.Archs.TeraScale_2,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac11,3": {
        "Board ID": "Mac-F2238BAE",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1,
            device_probe.AMD.Archs.TeraScale_2,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac12,1": {
        "Board ID": "Mac-942B5BF58194151B",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac12,2": {
        "Board ID": "Mac-942B59F58194171B",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "AAPL_iMac12,2": {
        # AppleInternal iMac12,2
        # True Model unknown
        "Board ID": "Mac-942B5B3A40C91381",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.sandy_bridge.value,
        "Max OS Supported": os_data.os_data.high_sierra,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Sandy_Bridge,
            device_probe.AMD.Archs.TeraScale_2,
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "iMac13,1": {
        "Board ID": "Mac-00BE6ED71E35EB86",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge,
            device_probe.NVIDIA.Archs.Kepler,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "mSATA"
        ],
    },
    "iMac13,2": {
        "Board ID": "Mac-FC02E91DDD3FA6A4",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge,
            device_probe.NVIDIA.Archs.Kepler,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "mSATA"
        ],
    },
    "iMac13,3": {
        "Board ID": "Mac-7DF2A3B5E5D671ED",
        "FirmwareFeatures": "0xE00DE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4360,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v1,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Ivy_Bridge,
            device_probe.NVIDIA.Archs.Kepler,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "mSATA"
        ],
    },
    "iMac14,1": {
        "Board ID": "Mac-031B6874CF7F642A",
        "FirmwareFeatures": "0xFB0FF577",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
            device_probe.NVIDIA.Archs.Kepler,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac14,2": {
        "Board ID": "Mac-27ADBB7B4CEE8E61",
        "FirmwareFeatures": "0xE00FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
            device_probe.NVIDIA.Archs.Kepler,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac14,3": {
        "Board ID": "Mac-77EB7D7DAF985301",
        "FirmwareFeatures": "0xE00FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.catalina,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
            device_probe.NVIDIA.Archs.Kepler,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac14,4": {
        "Board ID": "Mac-81E3E92DD6088272",
        "FirmwareFeatures": "0xF00FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac15,1": {
        "Board ID": "Mac-42FD25EABCABB274",
        "FirmwareFeatures": "0xF80FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
            device_probe.AMD.Archs.Legacy_GCN_7000,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac15,1_v2": {
        "Board ID": "Mac-FA842E06C61E91C5",
        "FirmwareFeatures": "0xF80FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.big_sur,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
            device_probe.AMD.Archs.Legacy_GCN_7000,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac16,1": {
        "Board ID": "Mac-A369DDC4E67F1C45",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.broadwell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Broadwell,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac16,2": {
        "Board ID": "Mac-FFE5EF870D7BA81A",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.broadwell.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Broadwell,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac17,1": {
        "Board ID": "Mac-DB15BD556843C820",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Skylake,
            device_probe.AMD.Archs.Legacy_GCN_9000,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac17,1_v2": {
        "Board ID": "Mac-65CE76090165799A",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Skylake,
            device_probe.AMD.Archs.Legacy_GCN_9000,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac17,1_v3": {
        "Board ID": "Mac-B809C3757DA9BB8D",
        "FirmwareFeatures": "0xFC0FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Skylake,
            device_probe.AMD.Archs.Legacy_GCN_9000,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac18,1": {
        "Board ID": "Mac-4B682C642B45593E",
        "FirmwareFeatures": "0xFD0FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.kaby_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Kaby_Lake,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac18,2": {
        "Board ID": "Mac-77F17D7DA9285301",
        "FirmwareFeatures": "0xFD0FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.kaby_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Kaby_Lake,
            device_probe.AMD.Archs.Polaris,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac18,3": {
        "Board ID": "Mac-BE088AF8C5EB4FA2",
        "FirmwareFeatures": "0xFD0FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.kaby_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20703,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Kaby_Lake,
            device_probe.AMD.Archs.Polaris,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac19,1": {
        "Board ID": "Mac-AA95B1DDAB278B95",
        "FirmwareFeatures": "0xFD8FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
            device_probe.AMD.Archs.Polaris,
            device_probe.AMD.Archs.Vega,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "AAPL_iMac19,1": {
        # AppleInternal iMac19,1 unit
        "Board ID": "Mac-CF21D135A7D34AA6",
        "FirmwareFeatures": "0xFD8FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
            device_probe.AMD.Archs.Polaris,
            device_probe.AMD.Archs.Vega,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac19,2": {
        "Board ID": "Mac-63001698E7A34814",
        "FirmwareFeatures": "0xFD8FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.Intel.Archs.Coffee_Lake,
            device_probe.AMD.Archs.Polaris,
            device_probe.AMD.Archs.Vega,
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe"
        ],
    },
    "iMac20,1": {
        "Board ID": "Mac-CFF7D910A743CAAF",
        "FirmwareFeatures": "0xFD8FF576",
        "SecureBootModel": "j185",
        "CPU Generation": cpu_data.cpu_data.comet_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Comet_Lake,
            device_probe.AMD.Archs.Navi,
        ],
        "Stock Storage": [
            "NVMe"
        ],
    },
    "iMac20,2": {
        "Board ID": "Mac-AF89B6D9451A490B",
        "FirmwareFeatures": "0xFD8FF576",
        "SecureBootModel": "j185f",
        "CPU Generation": cpu_data.cpu_data.comet_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Broadcom",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.Intel.Archs.Comet_Lake,
            device_probe.AMD.Archs.Navi,
        ],
        "Stock Storage": [
            "NVMe"
        ],
    },
    "iMac21,1": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j456",
        "CPU Generation": cpu_data.cpu_data.apple_m1.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe"
        ],
    },
    "iMac21,2": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j457",
        "CPU Generation": cpu_data.cpu_data.apple_m1.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe"
        ],
    },
    "iMacPro1,1": {
        "Board ID": "Mac-7BA5B2D9E42DDD94",
        "FirmwareFeatures": "0xFD8FF53E",
        "SecureBootModel": "j137",
        "CPU Generation": cpu_data.cpu_data.skylake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Aquantia",
        "5K Display": True,
        "Stock GPUs": [
            device_probe.AMD.Archs.Vega,
        ],
        "Stock Storage": [
            "NVMe"
        ],
    },
    "MacPro1,1": {
        "Board ID": "Mac-F4208DC8",
        "FirmwareFeatures": "0x80000015",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "UGA Graphics": True,
        "Ethernet Chipset": "Intel 80003ES2LAN",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Curie
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "MacPro2,1": {
        "Board ID": "Mac-F4208DA9",
        "FirmwareFeatures": "0xC0000015",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "UGA Graphics": True,
        "Ethernet Chipset": "Intel 80003ES2LAN",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Curie
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "MacPro3,1": {
        "Board ID": "Mac-F42C88C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm43224,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2045,
        "UGA Graphics": True,
        "Ethernet Chipset": "Intel 80003ES2LAN",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_1
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "MacPro4,1": {
        "Board ID": "Mac-F221BEC8",
        "FirmwareFeatures": "0xE001F537",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": device_probe.Atheros.Chipsets.AirPortAtheros40,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Intel 82574L",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "MacPro5,1": {
        "Board ID": "Mac-F221BEC8",
        "FirmwareFeatures": "0xE80FE137",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.mojave,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirPortBrcm4331,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM2046,
        "Ethernet Chipset": "Intel 82574L",
        "Stock GPUs": [
            device_probe.AMD.Archs.TeraScale_2
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "MacPro6,1": {
        "Board ID": "Mac-F60DEB81FF30ACF6",
        "FirmwareFeatures": "0xE90FF576",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.ivy_bridge.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [
            device_probe.AMD.Archs.Legacy_GCN_7000
        ],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "MacPro7,1": {
        "Board ID": "Mac-27AD2F918AE68F61",
        "FirmwareFeatures": "0xFDAFF066",
        "SecureBootModel": "j160",
        "CPU Generation": cpu_data.cpu_data.coffee_lake.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.UART,
        "Ethernet Chipset": "Aquantia",
        "Stock GPUs": [
            device_probe.AMD.Archs.Polaris,
            device_probe.AMD.Archs.Vega,
            device_probe.AMD.Archs.Navi
        ],
        "Stock Storage": [
            "SATA 3.5",
            "NVMe",
        ],
    },
    "Xserve1,1": {
        "Board ID": "Mac-F4208AC8",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.conroe.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "UGA Graphics": True,
        "Ethernet Chipset": "Intel 80003ES2LAN",
        "Stock GPUs": [
            device_probe.AMD.Archs.R500
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "Xserve2,1": {
        "Board ID": "Mac-F42289C8",
        "FirmwareFeatures": "0xC0001403",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.lion,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "UGA Graphics": True,
        "Ethernet Chipset": "Intel 80003ES2LAN",
        "Stock GPUs": [
            device_probe.AMD.Archs.R500
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "Xserve3,1": {
        "Board ID": "Mac-F223BEC8",
        "FirmwareFeatures": "0xE001F537",
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.nehalem.value,
        "Max OS Supported": os_data.os_data.el_capitan,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "Ethernet Chipset": "Intel 82574L",
        "Stock GPUs": [
            device_probe.NVIDIA.Archs.Tesla
        ],
        "Stock Storage": [
            "SATA 3.5",
        ],
    },
    "ADP2,1": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.pentium_4.value,
        "Max OS Supported": os_data.os_data.leopard,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "Stock GPUs": [
            device_probe.Intel.Archs.GMA_950
        ],
        "Stock Storage": [
            "SATA 3.5",
            "PATA",
        ],
    },
    "ADP3,2": {
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j273a",
        "CPU Generation": cpu_data.cpu_data.apple_dtk.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": device_probe.Broadcom.Chipsets.AppleBCMWLANBusInterfacePCIe,
        "Bluetooth Model": bluetooth_data.bluetooth_data.PCIe,
        "Ethernet Chipset": "Broadcom",
        "Stock GPUs": [],
        "Stock Storage": [
            "NVMe",
        ],
    },
    "AAPLJ53,1": {
        # AppleInternal MacBookPro11,4
        "Board ID": "Mac-C08A65A66A9A3BA2",
        "FirmwareFeatures": None,
        "SecureBootModel": None,
        "CPU Generation": cpu_data.cpu_data.haswell.value,
        "Max OS Supported": os_data.os_data.mavericks,
        "Wireless Model": device_probe.Broadcom.Chipsets.AirportBrcmNIC,
        "Bluetooth Model": bluetooth_data.bluetooth_data.BRCM20702_v2,
        "Stock GPUs": [
            device_probe.Intel.Archs.Haswell,
        ],
        "Stock Storage": [
            "NVMe",
        ],

    },
    "Intel Virtual Machine": {
        "Board ID": "VMM-x86_64",
        "FirmwareFeatures": None,
        "SecureBootModel": "x86legacy",
        "CPU Generation": cpu_data.cpu_data.penryn.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "Stock GPUs": [],
        "Stock Storage": [],
    },
    "VirtualMac1,1": {
        # Apple Silicon Virtual Machine
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "vma1macos",
        "CPU Generation": cpu_data.cpu_data.apple_m1.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "Stock GPUs": [],
        "Stock Storage": [],
    },
    "VirtualMac2,1": {
        # Apple Silicon Virtual Machine
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "vma2macos",
        "CPU Generation": cpu_data.cpu_data.apple_m1.value,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "Stock GPUs": [],
        "Stock Storage": [],
    },
    "iBridge2,11": {
        # Unknown ID, Intel based, present in Monterey
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j230",
        "CPU Generation": None,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "Stock GPUs": [],
        "Stock Storage": [],
    },
    "iBridge2,13": {
        # Unknown ID, Intel based, present in Monterey
        "Board ID": None,
        "FirmwareFeatures": None,
        "SecureBootModel": "j214",
        "CPU Generation": None,
        "Max OS Supported": os_data.os_data.max_os,
        "Wireless Model": None,
        "Bluetooth Model": bluetooth_data.bluetooth_data.NonApplicable,
        "Stock GPUs": [],
        "Stock Storage": [],
    },
}
