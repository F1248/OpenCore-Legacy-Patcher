#!/usr/bin/env python3
# Simple script to delete unnecessary files from OpenCore and move into place
# To use, simply :
# - Download OpenCore-{VERSION}-{VARIANT}.zip
#   - https://github.com/acidanthera/OpenCorePkg/releases
# - Place zips in same directory as this script
# - Run script
# TODO:
# - Download latest builds from dortania.github.io

import subprocess
from pathlib import Path

BUILD_VARIANTS = [
    "DEBUG",
    "RELEASE"
]

UNUSED_DRIVERS = [
    "AudioDxe.efi",
    "BiosVideo.efi",
    "CrScreenshotDxe.efi",
    "Ext4Dxe.efi",
    "HiiDatabase.efi",
    "NvmExpressDxe.efi",
    "OpenHfsPlus.efi",
    "OpenNtfsDxe.efi",
    "OpenPartitionDxe.efi",
    "OpenUsbKbDxe.efi",
    "OpenVariableRuntimeDxe.efi",
    "Ps2KeyboardDxe.efi",
    "Ps2MouseDxe.efi",
    "ToggleSipEntry.efi",
    "UsbMouseDxe.efi",
    "XhciDxe.efi",
    "Udp4Dxe.efi",
    "TcpDxe.efi",
    "SnpDxe.efi",
    "MnpDxe.efi",
    "Ip4Dxe.efi",
    "HttpUtilitiesDxe.efi",
    "HttpDxe.efi",
    "HttpBootDxe.efi",
    "DpcDxe.efi",
    "DnsDxe.efi",
    "Dhcp4Dxe.efi",
    "ArpDxe.efi",
]

UNUSED_TOOLS = [
    "ChipTune.efi",
    "CleanNvram.efi",
    "ControlMsrE2.efi",
    "GopStop.efi",
    "KeyTester.efi",
    "MmapDump.efi",
    "OpenControl.efi",
    "ResetSystem.efi",
    "RtcRw.efi",
    "CsrUtil.efi",
    "TpmInfo.efi",
]

IMPORTANT_UTILITIES = [
    "macserial",
    "ocvalidate",
]



class GenerateOpenCore:

    def __init__(self):
        print("Generating new OpenCore bundles...")

        self.working_dir = None

        self.set_directory()
        self.validate_files()
        self.generate()

        print("New OpenCore bundles generated!")

    def set_directory(self):
        self.working_dir = Path(__file__).parent.absolute()
        print(f"Working directory: {self.working_dir}")

        self.debug_zip = None
        self.release_zip = None

        # Find OpenCore DEBUG zip
        for file in self.working_dir.iterdir():
            if file.name.endswith(".zip") and "DEBUG" in file.name:
                print(f"   Found DEBUG zip: {file.name}")
                self.debug_zip = file

        # Find OpenCore RELEASE zip
        for file in self.working_dir.iterdir():
            if file.name.endswith(".zip") and "RELEASE" in file.name:
                print(f"   Found RELEASE zip: {file.name}")
                self.release_zip = file

        if self.debug_zip is None:
            raise FileNotFoundError("DEBUG zip not found!")

        if self.release_zip is None:
            raise FileNotFoundError("RELEASE zip not found!")


        # Unzip both, rename to OpenCore-DEBUG and OpenCore-RELEASE
        print("Unzipping DEBUG zip...")
        subprocess.run (
            ["unzip", f"{self.debug_zip}", "-d", f"{self.working_dir}/OpenCore-DEBUG-ROOT"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        print("Unzipping RELEASE zip...")
        subprocess.run (
            ["unzip", f"{self.release_zip}", "-d", f"{self.working_dir}/OpenCore-RELEASE-ROOT"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        for variant in BUILD_VARIANTS:
            print(f"Moving {variant} folder...")
            subprocess.run (
                ["mv", f"{self.working_dir}/OpenCore-{variant}-ROOT/X64", f"{self.working_dir}/OpenCore-{variant}"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            if variant == "DEBUG":
                for utility in IMPORTANT_UTILITIES:
                    print(f"Moving {utility} from {variant} variant...")
                    subprocess.run (
                        ["rm", "-rf", f"{self.working_dir}/{utility}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                    subprocess.run (
                        ["mv", f"{self.working_dir}/OpenCore-{variant}-ROOT/Utilities/{utility}/{utility}", f"{self.working_dir}/{utility}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )

            # Remove root folder
            subprocess.run (
                ["rm", "-rf", f"{self.working_dir}/OpenCore-{variant}-ROOT"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

        # Remove zip files
        print("Removing zip files...")
        # remove debug_zip
        subprocess.run (
            ["rm", "-rf", self.debug_zip],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        # remove release_zip
        subprocess.run (
            ["rm", "-rf", self.release_zip],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )


    def clean_old_bundles(self):
        print("Cleaning old bundles...")
        for variant in BUILD_VARIANTS:
            if (self.working_dir / f"OpenCore-{variant}").exists():
                print(f"   Deleting old {variant} variant...")
                subprocess.run (
                    ["rm", "-rf", f"{self.working_dir}/OpenCore-{variant}"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )

    def validate_files(self):
        for variant in BUILD_VARIANTS:
            if not (self.working_dir / f"OpenCore-{variant}").exists():
                raise FileNotFoundError(f"OpenCore-{variant} folder not found!")

    def generate(self):
        for variant in BUILD_VARIANTS:
            print(f"Generating {variant} variant...")
            self.generate_opencore(variant)

    def generate_opencore(self, variant):
        # Create S/L/C
        print("   Creating SLC folder")
        subprocess.run (
            ["mkdir", "-p", f"{self.working_dir}/OpenCore-{variant}/System/Library/CoreServices"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Relocate contents of /EFI/BOOT to /S/L/C
        print("   Relocating BOOT folder to SLC")
        for file in (self.working_dir / f"OpenCore-{variant}/EFI/BOOT").iterdir():
            subprocess.run (
                ["mv", f"{file}", f"{self.working_dir}/OpenCore-{variant}/System/Library/CoreServices"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

        # Rename BOOTx64.efi to boot.efi
        print("   Renaming BOOTx64.efi to boot.efi")
        subprocess.run (
            ["mv", f"{self.working_dir}/OpenCore-{variant}/System/Library/CoreServices/BOOTx64.efi", f"{self.working_dir}/OpenCore-{variant}/System/Library/CoreServices/boot.efi"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Delete BOOT folder
        print("   Deleting BOOT folder")
        subprocess.run (
            ["rm", "-rf", f"{self.working_dir}/OpenCore-{variant}/EFI/BOOT"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Delete unused drivers
        print("   Deleting unused drivers")
        for driver in UNUSED_DRIVERS:
            if Path(f"{self.working_dir}/OpenCore-{variant}/EFI/OC/Drivers/{driver}").exists():
                print(f"      Deleting {driver}")
                subprocess.run (
                    ["rm", f"{self.working_dir}/OpenCore-{variant}/EFI/OC/Drivers/{driver}"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            else:
                print(f"      {driver} not found")

        # Delete unused tools
        print("   Deleting unused tools")
        for tool in UNUSED_TOOLS:
            if Path(f"{self.working_dir}/OpenCore-{variant}/EFI/OC/Tools/{tool}").exists():
                print(f"      Deleting {tool}")
                subprocess.run (
                    ["rm", f"{self.working_dir}/OpenCore-{variant}/EFI/OC/Tools/{tool}"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            else:
                print(f"      {tool} not found")

        # Rename OpenCore-<variant> to OpenCore-Build
        print("   Renaming OpenCore folder")
        subprocess.run (
            ["mv", f"{self.working_dir}/OpenCore-{variant}", f"{self.working_dir}/OpenCore-Build"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Create OpenCore-<variant>.zip
        print("   Creating OpenCore.zip")
        subprocess.run (
            ["ditto", "-c", "-k", "--sequesterRsrc", "--keepParent", f"{self.working_dir}/OpenCore-Build", f"{self.working_dir}/OpenCore-{variant}.zip"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Delete OpenCore-Build
        print("   Deleting OpenCore-Build")
        subprocess.run (
            ["rm", "-rf", f"{self.working_dir}/OpenCore-Build"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )


if __name__ == "__main__":
    GenerateOpenCore()