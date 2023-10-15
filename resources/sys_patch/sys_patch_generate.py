# Generate patch set for use in sys_patch.py
import logging

from resources import constants, utilities, device_probe
from data import sys_patch_dict

class GenerateRootPatchSets:
    """
    Library for generating patch sets for the current host

    Parameters:
        model (str): Model identifier
        global_constants (constants.Constants): Global constants object
        hardware_details (dict): Dictionary of hardware details generated by detect_patch_set()

    Usage:
        >>> from resources.sys_patch import sys_patch_generate
        >>> patchset = sys_patch_generate.GenerateRootPatches("iMac7,1", self.constants, self.hardware_details).patchset

    """

    def __init__(self, model: str, global_constants: constants.Constants, hardware_details: dict) -> None:
        self.model: str = model
        self.constants: constants.Constants = global_constants
        self.hardware_details:  dict = hardware_details

        self.patchset: dict = self._generate_patchset()


    def _generate_patchset(self) -> dict:
        """
        Generate Patchset dictionary for the current system

        Returns:
            dict: Dictionary of patches to be applied from sys_patch_dict.py
        """

        all_hardware_patchset: dict = sys_patch_dict.SystemPatchDictionary(self.constants.detected_os, self.constants.detected_os_minor, self.constants.legacy_accel_support).patchset_dict
        required_patches:      dict = {}

        utilities.cls()

        logging.info("The following patches will be applied:")

        if self.hardware_details["Graphics: Intel Ironlake"] is True:
            required_patches.update({"Non-Metal Common": all_hardware_patchset["Graphics"]["Non-Metal Common"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"Intel Ironlake": all_hardware_patchset["Graphics"]["Intel Ironlake"]})

        if self.hardware_details["Graphics: Intel Sandy Bridge"] is True:
            required_patches.update({"Non-Metal Common": all_hardware_patchset["Graphics"]["Non-Metal Common"]})
            required_patches.update({"High Sierra GVA": all_hardware_patchset["Graphics"]["High Sierra GVA"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"Intel Sandy Bridge": all_hardware_patchset["Graphics"]["Intel Sandy Bridge"]})
            # Patchset breaks Display Profiles, don't install if primary GPU is AMD. Give users option to disable patch in settings to restore Display Profiles
            if self.constants.computer.real_model not in ["Macmini5,2", "iMac12,1", "iMac12,2"]:
                required_patches.update({"Revert Non-Metal ColorSync Workaround": all_hardware_patchset["Graphics"]["Revert Non-Metal ColorSync Workaround"]})

        if self.hardware_details["Graphics: Intel Ivy Bridge"] is True:
            required_patches.update({"Metal 3802 Common": all_hardware_patchset["Graphics"]["Metal 3802 Common"]})
            required_patches.update({"Metal 3802 Common Extended": all_hardware_patchset["Graphics"]["Metal 3802 Common Extended"]})
            required_patches.update({"Catalina GVA": all_hardware_patchset["Graphics"]["Catalina GVA"]})
            required_patches.update({"Monterey OpenCL": all_hardware_patchset["Graphics"]["Monterey OpenCL"]})
            required_patches.update({"Big Sur OpenCL": all_hardware_patchset["Graphics"]["Big Sur OpenCL"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"Intel Ivy Bridge": all_hardware_patchset["Graphics"]["Intel Ivy Bridge"]})

        if self.hardware_details["Graphics: Intel Haswell"] is True:
            required_patches.update({"Metal 3802 Common": all_hardware_patchset["Graphics"]["Metal 3802 Common"]})
            required_patches.update({"Metal 3802 Common Extended": all_hardware_patchset["Graphics"]["Metal 3802 Common Extended"]})
            required_patches.update({"Monterey GVA": all_hardware_patchset["Graphics"]["Monterey GVA"]})
            required_patches.update({"Monterey OpenCL": all_hardware_patchset["Graphics"]["Monterey OpenCL"]})
            required_patches.update({"Intel Haswell": all_hardware_patchset["Graphics"]["Intel Haswell"]})

        if self.hardware_details["Graphics: Intel Broadwell"] is True:
            required_patches.update({"Monterey GVA": all_hardware_patchset["Graphics"]["Monterey GVA"]})
            required_patches.update({"Monterey OpenCL": all_hardware_patchset["Graphics"]["Monterey OpenCL"]})
            required_patches.update({"Intel Broadwell": all_hardware_patchset["Graphics"]["Intel Broadwell"]})

        if self.hardware_details["Graphics: Intel Skylake"] is True:
            required_patches.update({"Revert GVA Downgrade": all_hardware_patchset["Graphics"]["Revert GVA Downgrade"]})
            required_patches.update({"Monterey OpenCL": all_hardware_patchset["Graphics"]["Monterey OpenCL"]})
            required_patches.update({"Intel Skylake": all_hardware_patchset["Graphics"]["Intel Skylake"]})

        if self.hardware_details["Graphics: Nvidia Tesla"] is True:
            required_patches.update({"Non-Metal Common": all_hardware_patchset["Graphics"]["Non-Metal Common"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"Nvidia Tesla": all_hardware_patchset["Graphics"]["Nvidia Tesla"]})

        if self.hardware_details["Graphics: Nvidia Web Drivers"] is True:
            required_patches.update({"Non-Metal Common": all_hardware_patchset["Graphics"]["Non-Metal Common"]})
            required_patches.update({"Non-Metal IOAccelerator Common": all_hardware_patchset["Graphics"]["Non-Metal IOAccelerator Common"]})
            required_patches.update({"Non-Metal CoreDisplay Common": all_hardware_patchset["Graphics"]["Non-Metal CoreDisplay Common"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"Nvidia Web Drivers": all_hardware_patchset["Graphics"]["Nvidia Web Drivers"]})
            required_patches.update({"Non-Metal Enforcement": all_hardware_patchset["Graphics"]["Non-Metal Enforcement"]})

        if self.hardware_details["Graphics: Nvidia Kepler"] is True:
            required_patches.update({"Metal 3802 Common": all_hardware_patchset["Graphics"]["Metal 3802 Common"]})
            required_patches.update({"Metal 3802 Common Extended": all_hardware_patchset["Graphics"]["Metal 3802 Common Extended"]})
            required_patches.update({"Catalina GVA": all_hardware_patchset["Graphics"]["Catalina GVA"]})
            required_patches.update({"Monterey OpenCL": all_hardware_patchset["Graphics"]["Monterey OpenCL"]})
            required_patches.update({"Big Sur OpenCL": all_hardware_patchset["Graphics"]["Big Sur OpenCL"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"Nvidia Kepler": all_hardware_patchset["Graphics"]["Nvidia Kepler"]})
            for gpu in self.constants.computer.gpus:
                # Handle mixed GPU situations (ie. MacBookPro11,3: Haswell iGPU + Kepler dGPU)
                if gpu.arch == device_probe.Intel.Archs.Haswell:
                    if "Catalina GVA" in required_patches:
                        del(required_patches["Catalina GVA"])
                    break

        if self.hardware_details["Graphics: AMD TeraScale 1"] is True:
            required_patches.update({"Non-Metal Common": all_hardware_patchset["Graphics"]["Non-Metal Common"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"AMD TeraScale Common": all_hardware_patchset["Graphics"]["AMD TeraScale Common"]})
            required_patches.update({"AMD TeraScale 1": all_hardware_patchset["Graphics"]["AMD TeraScale 1"]})

        if self.hardware_details["Graphics: AMD TeraScale 2"] is True:
            required_patches.update({"Non-Metal Common": all_hardware_patchset["Graphics"]["Non-Metal Common"]})
            required_patches.update({"Non-Metal IOAccelerator Common": all_hardware_patchset["Graphics"]["Non-Metal IOAccelerator Common"]})
            required_patches.update({"WebKit Monterey Common": all_hardware_patchset["Graphics"]["WebKit Monterey Common"]})
            required_patches.update({"AMD TeraScale Common": all_hardware_patchset["Graphics"]["AMD TeraScale Common"]})
            required_patches.update({"AMD TeraScale 2": all_hardware_patchset["Graphics"]["AMD TeraScale 2"]})
            if self.constants.allow_ts2_accel is False or self.constants.detected_os not in self.constants.legacy_accel_support:
                # TeraScale 2 MacBooks with faulty GPUs are highly prone to crashing with AMDRadeonX3000 attached
                # Additionally, AMDRadeonX3000 requires IOAccelerator downgrade which is not installed without 'Non-Metal IOAccelerator Common'
                del(required_patches["AMD TeraScale 2"]["Install"]["/System/Library/Extensions"]["AMDRadeonX3000.kext"])

        if self.hardware_details["Graphics: AMD Legacy GCN"] is True or self.hardware_details["Graphics: AMD Legacy Polaris"] is True:
            if self.hardware_details["Graphics: Intel Skylake"] is False:
                # GVA downgrade not required if Skylake is present
                required_patches.update({"Monterey GVA": all_hardware_patchset["Graphics"]["Monterey GVA"]})
            required_patches.update({"Monterey OpenCL": all_hardware_patchset["Graphics"]["Monterey OpenCL"]})
            if self.hardware_details["Graphics: AMD Legacy GCN"] is True:
                required_patches.update({"AMD Legacy GCN": all_hardware_patchset["Graphics"]["AMD Legacy GCN"]})
            else:
                required_patches.update({"AMD Legacy Polaris": all_hardware_patchset["Graphics"]["AMD Legacy Polaris"]})
                required_patches.update({"Revert GVA Downgrade": all_hardware_patchset["Graphics"]["Revert GVA Downgrade"]})
            if "AVX2" not in self.constants.computer.cpu.leafs:
                required_patches.update({"AMD OpenCL": all_hardware_patchset["Graphics"]["AMD OpenCL"]})
        if self.hardware_details["Graphics: AMD Legacy GCN (2017)"] is True:
            required_patches.update({"AMD Legacy GCN v2": all_hardware_patchset["Graphics"]["AMD Legacy GCN v2"]})

        if self.hardware_details["Graphics: AMD Legacy Vega"] is True:
            required_patches.update({"Monterey GVA": all_hardware_patchset["Graphics"]["Monterey GVA"]})
            required_patches.update({"Monterey OpenCL": all_hardware_patchset["Graphics"]["Monterey OpenCL"]})
            required_patches.update({"AMD Legacy Vega": all_hardware_patchset["Graphics"]["AMD Legacy Vega"]})
            required_patches.update({"AMD OpenCL": all_hardware_patchset["Graphics"]["AMD OpenCL"]})
            if self.hardware_details["Graphics: AMD Legacy GCN"] is True:
                required_patches.update({"AMD Legacy Vega Extended": all_hardware_patchset["Graphics"]["AMD Legacy Vega Extended"]})
            else:
                required_patches.update({"Revert GVA Downgrade": all_hardware_patchset["Graphics"]["Revert GVA Downgrade"]})

        if self.hardware_details["Brightness: Legacy Backlight Control"] is True:
            required_patches.update({"Legacy Backlight Control": all_hardware_patchset["Brightness"]["Legacy Backlight Control"]})

        if self.hardware_details["Audio: Legacy Realtek"] is True:
            if self.model in ["iMac7,1", "iMac8,1"]:
                required_patches.update({"Legacy Realtek": all_hardware_patchset["Audio"]["Legacy Realtek"]})
            else:
                required_patches.update({"Legacy Non-GOP": all_hardware_patchset["Audio"]["Legacy Non-GOP"]})

        if self.hardware_details["Networking: Legacy Wireless"] is True:
            required_patches.update({"Legacy Wireless": all_hardware_patchset["Networking"]["Legacy Wireless"]})
            required_patches.update({"Legacy Wireless Extended": all_hardware_patchset["Networking"]["Legacy Wireless Extended"]})

        if self.hardware_details["Networking: Modern Wireless"] is True:
            required_patches.update({"Legacy Wireless": all_hardware_patchset["Networking"]["Modern Wireless"]})

        if self.hardware_details["Miscellaneous: Legacy GMUX"] is True:
            required_patches.update({"Legacy GMUX": all_hardware_patchset["Miscellaneous"]["Legacy GMUX"]})

        if self.hardware_details["Miscellaneous: Legacy Keyboard Backlight"] is True:
            required_patches.update({"Legacy Keyboard Backlight": all_hardware_patchset["Miscellaneous"]["Legacy Keyboard Backlight"]})

        if self.hardware_details["Miscellaneous: Legacy USB 1.1"] is True:
            required_patches.update({"Legacy USB 1.1": all_hardware_patchset["Miscellaneous"]["Legacy USB 1.1"]})
            required_patches.update({"Legacy USB 1.1 Extended": all_hardware_patchset["Miscellaneous"]["Legacy USB 1.1 Extended"]})

        if self.hardware_details["Miscellaneous: PCIe FaceTime Camera"] is True:
            required_patches.update({"PCIe FaceTime Camera": all_hardware_patchset["Miscellaneous"]["PCIe FaceTime Camera"]})

        if self.hardware_details["Miscellaneous: T1 Security Chip"] is True:
            required_patches.update({"T1 Security Chip": all_hardware_patchset["Miscellaneous"]["T1 Security Chip"]})

        if required_patches:
            host_os_float = float(f"{self.constants.detected_os}.{self.constants.detected_os_minor}")

            # Prioritize Monterey GVA patches
            if "Catalina GVA" in required_patches and "Monterey GVA" in required_patches:
                del(required_patches["Catalina GVA"])

            for patch_name in list(required_patches):
                patch_os_min_float = float(f'{required_patches[patch_name]["OS Support"]["Minimum OS Support"]["OS Major"]}.{required_patches[patch_name]["OS Support"]["Minimum OS Support"]["OS Minor"]}')
                patch_os_max_float = float(f'{required_patches[patch_name]["OS Support"]["Maximum OS Support"]["OS Major"]}.{required_patches[patch_name]["OS Support"]["Maximum OS Support"]["OS Minor"]}')
                if (host_os_float < patch_os_min_float or host_os_float > patch_os_max_float):
                    del(required_patches[patch_name])
                else:
                    if required_patches[patch_name]["Display Name"]:
                        logging.info(f"- {required_patches[patch_name]['Display Name']}")
        else:
            logging.info("- No patch sets found for booted model")

        return required_patches