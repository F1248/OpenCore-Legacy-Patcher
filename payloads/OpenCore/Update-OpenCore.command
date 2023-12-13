#!/usr/bin/env python3.13

# Script to download and generate valid OpenCorePkg folder/file structure for use with OpenCore Legacy Patcher
# To use:
# - Download OpenCore-{VERSION}-{VARIANT}.zip
#   - If no files are found, the script will download the latest version
# - Place zips in same directory as this script
# - Run script


import subprocess
from pathlib import Path

NIGHTLY_URL = "https://nightly.link/acidanthera/OpenCorePkg/workflows/build/master/macOS%20XCODE5%20Artifacts.zip"

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
    "ListPartitions.efi",
    "FontTester.efi",
]

IMPORTANT_UTILITIES = [
    "macserial",
    "ocvalidate",
]



class GenerateOpenCore:

    def __init__(self):
        print("Generating new OpenCore bundles…")

        self.working_dir = None

        self.set_directory()
        self.validate_files()
        self.generate()

        print("New OpenCore bundles generated!")

    def set_directory(self):
        self.working_dir = Path(__file__).parent.absolute()
        print(f"Working directory: {self.working_dir}")

        self.zip_files = {}
        self.download_binaries()

        # Unzip and reanme
        for variant in BUILD_VARIANTS:
            print(f"Unzipping {variant}…")
            subprocess.run (
                ["unzip", self.zip_files[variant], "-d", f"{self.working_dir}/OpenCore-{variant}-ROOT"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            print(f"Moving {variant} folder…")
            subprocess.run (
                ["mv", f"{self.working_dir}/OpenCore-{variant}-ROOT/X64", f"{self.working_dir}/OpenCore-{variant}"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            if variant == "DEBUG":
                for utility in IMPORTANT_UTILITIES:
                    print(f"Moving {utility} from {variant} variant…")
                    subprocess.run (
                        ["rm", "-rf", f"{self.working_dir}/{utility}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                    subprocess.run (
                        ["mv", f"{self.working_dir}/OpenCore-{variant}-ROOT/Utilities/{utility}/{utility}", f"{self.working_dir}/{utility}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )

            # Delete root folder
            subprocess.run (
                ["rm", "-rf", f"{self.working_dir}/OpenCore-{variant}-ROOT"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            # Delete zip files
            print(f"Deleting {variant} zip…")
            subprocess.run (
                ["rm", "-rf", self.zip_files[variant]],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

    def download_binaries(self):

        print("Downloading latest nightly build…")
        zip_path = f"{self.working_dir}/macOS XCODE5 Artifacts.zip"
        subprocess.run (
            ["curl", "-L", NIGHTLY_URL, "-o", zip_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print("Unzipping and deleting macOS XCODE5 Artifacts.zip…")
        subprocess.run (
            ["unzip", zip_path, "-d", self.working_dir],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        subprocess.run (
            ["rm", zip_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        print("Verifying Zips…")
        for variant in BUILD_VARIANTS:
            for file in self.working_dir.iterdir():
                if file.name.endswith(f"{variant}.zip") and file.name != f"OpenCore-{variant}.zip":
                    print(f"   Found {variant} zip: {file.name}")
                    self.zip_files[variant] = file
                    break
            else:
                raise Exception(f"Variant {variant} missing")

    def clean_old_bundles(self):
        print("Cleaning old bundles…")
        for variant in BUILD_VARIANTS:
            if (self.working_dir / f"OpenCore-{variant}").exists():
                print(f"   Deleting old {variant} variant…")
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
            print(f"Generating {variant} variant…")
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
                ["mv", file, f"{self.working_dir}/OpenCore-{variant}/System/Library/CoreServices"],
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