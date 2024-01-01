#!/usr/bin/env python3.12

# Generate stand alone application for OpenCore Legacy Patcher
# Copyright (C) 2022-2023 - Mykola Grymalyuk

import os
import time
import argparse
import plistlib
import subprocess

from pathlib import Path

from resources import constants


class CreateBinary:
    """
    Library for creating OpenCore Legacy Patcher application

    This script's main purpose is to handle the following:
       - Download external dependencies (ex. PatcherSupportPkg)
       - Convert payloads directory into DMG
       - Build Binary via PyInstaller
       - Patch 'LC_VERSION_MIN_MACOSX' to OS X 10.10
       - Add build arguments to Info.plist
    """

    def __init__(self):
        start = time.time()
        self._set_cwd()

        print("Starting build script")
        self.args = self._parse_arguments()

        print(f"Current Working Directory:\n- {os.getcwd()}")

        self._preflight_processes()
        self._build_binary()
        self._postflight_processes()
        print(f"Build script completed in {round(time.time() - start)} seconds")


    def _set_cwd(self):
        """
        Initialize current working directory to parent of this script
        """

        os.chdir(Path(__file__).resolve().parent)


    def _parse_arguments(self):
        """
        Parse arguments passed to script
        """

        parser = argparse.ArgumentParser(description="Builds OpenCore Legacy Patcher")
        parser.add_argument("--date_time", type=str, help="Commit or build date and time")
        parser.add_argument("--repository", type=str, help="Git repository")
        parser.add_argument("--branch", type=str, help="Git branch")
        parser.add_argument("--commit_url", type=str, help="Git commit URL")
        args = parser.parse_args()
        return args


    def _preflight_processes(self):
        """
        Start preflight processes
        """

        print("Starting preflight processes")
        self._setup_pathing()
        self._delete_extra_binaries()
        self._download_universal_binaries()
        self._generate_payloads_dmg()


    def _postflight_processes(self):
        """
        Start postflight processes
        """

        print("Starting postflight processes")
        self._patch_load_command()
        self._add_build_arguments()
        self._post_flight_cleanup()


    def _build_binary(self):
        """
        Build binary via PyInstaller
        """

        print("Building GUI binary…")
        build_args = [self.pyinstaller_path, "./PyInstaller.spec", "--noconfirm"]

        build_result = subprocess.run(build_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if build_result.returncode != 0:
            print("Build failed")
            print(build_result.stderr.decode('utf-8'))
            raise Exception("Build failed")

        # Next embed support icns into ./Resources
        print("Embedding icns…")
        for file in Path("payloads/Icon/AppIcons").glob("*.icns"):
            subprocess.run(
                ["/bin/cp", str(file), "./dist/OpenCore Legacy Patcher.app/Contents/Resources/"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )


    def _setup_pathing(self):
        """
        Initialize pathing for PyInstaller
        """

        pyinstaller_path = "/Library/Frameworks/Python.framework/Versions/3.12/bin/pyinstaller"

        if not Path(pyinstaller_path).exists():
            print(f"- PyInstaller not found:\n\t{pyinstaller_path}")
            raise Exception("PyInstaller not found")

        self.pyinstaller_path = pyinstaller_path


    def _delete_extra_binaries(self):
        """
        Delete extra binaries from payloads directory
        """

        whitelist_folders = [
            "ACPI",
            "Config",
            "Drivers",
            "Icon",
            "InstallPackage",
            "Kexts",
            "OpenCore",
            "Tools",
            "Launch Services",
        ]

        whitelist_files = [
            "entitlements.plist",
            "launcher.sh",
            "OpenCore-Legacy-Patcher.icns",
        ]


        print("Deleting extra binaries…")
        for file in Path("payloads").glob(pattern="*"):
            if file.is_dir():
                if file.name in whitelist_folders:
                    continue
                print(f"- Deleting {file.name}")
                subprocess.run(["/bin/rm", "-rf", file])
            else:
                if file.name in whitelist_files:
                    continue
                print(f"- Deleting {file.name}")
                subprocess.run(["/bin/rm", "-f", file])


    def _download_universal_binaries(self):
        """
        Download Universal-Binaries.dmg
        """

        print("Downloading Universal-Binaries.dmg…")
        if Path("./Universal-Binaries.dmg").exists():
            print("Universal-Binaries.dmg already exists, skipping download")
            return
        print(f"- Downloading Universal-Binaries.dmg…")

        download_result = subprocess.run(["/usr/bin/curl", "--location", constants.Constants().support_url, "--remote-name"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if download_result.returncode != 0:
            print(f"Failed to download Universal%20Binaries.zip. Error: {download_result.stderr.decode('utf-8')}")
            raise Exception("Download failed")
        if not Path("./Universal%20Binaries.zip").exists():
            print("- Universal%20Binaries.zip not found")
            raise Exception("Universal%20Binaries.zip not found")

        unzip_result = subprocess.run(["/usr/bin/ditto", "-xk", "Universal%20Binaries.zip", "./"], capture_output=True)
        if unzip_result.returncode != 0:
            print(f"Failed to extract Universal%20Binaries.zip. Error: {unzip_result.stderr.decode('utf-8')}")
            raise Exception("Unzip failed")
        if not Path("./Universal-Binaries.dmg").exists():
            print("- Universal-Binaries.dmg not found")
            raise Exception("Universal-Binaries.dmg not found")


    def _generate_payloads_dmg(self):
        """
        Generate disk image containing all payloads
        Disk image will be password protected due to issues with
        Apple's notarization system and inclusion of kernel extensions
        """

        print("- Generating DMG…")
        dmg_output = subprocess.run([
            '/usr/bin/hdiutil', 'create', './payloads.dmg',
            '-megabytes', '32000',  # Overlays can only be as large as the disk image allows
            '-format', 'UDZO', '-ov',
            '-volname', 'OpenCore Legacy Patcher Resources (Base)',
            '-fs', 'HFS+',
            '-srcfolder', './payloads',
            '-passphrase', 'password', '-encryption',
            '-verbose'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if dmg_output.returncode != 0:
            print("- DMG generation failed")
            print(dmg_output.stderr.decode('utf-8'))
            raise Exception("DMG generation failed")

        print("- DMG generation complete")


    def _patch_load_command(self):
        """
        Patch LC_VERSION_MIN_MACOSX in Load Command to report 10.10

        By default PyInstaller will create binaries supporting 10.13+
        However this limitation is entirely arbitrary for our libraries
        and instead we're able to support 10.10 without issues.

        To verify set version:
          otool -l ./dist/OpenCore Legacy Patcher.app/Contents/MacOS/OpenCore-Legacy-Patcher

              cmd LC_VERSION_MIN_MACOSX
          cmdsize 16
          version 10.13
              sdk 10.9
        """

        print("- Patching LC_VERSION_MIN_MACOSX")
        path = "./dist/OpenCore Legacy Patcher.app/Contents/MacOS/OpenCore-Legacy-Patcher"
        find = b"\x00\x0D\x0A\x00" # 10.13 (0xA0D)
        replace = b"\x00\x0A\x0A\x00" # 10.10 (0xA0A)
        with open(path, 'rb') as f:
            data = f.read()
            data = data.replace(find, replace, 1)
            with open(path, 'wb') as f:
                f.write(data)


    def _add_build_arguments(self):
        """
        Add build arguments to Info.plist
        """

        print("- Adding build arguments to Info.plist")
        plist_path = Path("./dist/OpenCore Legacy Patcher.app/Contents/Info.plist")
        plist = plistlib.load(Path(plist_path).open("rb"))

        plist["Build arguments"] = {}

        if self.args.date_time:
            date_time = self.args.date_time
        else:
            date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        plist["Build arguments"]["Date and time"] = date_time

        if self.args.repository:
            repository = self.args.repository
            plist["Build arguments"]["Repository"] = repository

        if self.args.branch:
            branch = self.args.branch.replace("refs/heads/", "")
            plist["Build arguments"]["Branch"] = branch

        if self.args.commit_url:
            commit_url = self.args.commit_url
            plist["Build arguments"]["Commit URL"] = commit_url

        plistlib.dump(plist, Path(plist_path).open("wb"), sort_keys=True)


    def _post_flight_cleanup(self):
        """
        Post flight cleanup
        """

        path = "./dist/OpenCore-Legacy-Patcher"
        print(f"- Removing {path}")
        rm_output = subprocess.run(
            ["/bin/rm", "-rf", path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if rm_output.returncode != 0:
            print(f"- Remove failed: {path}")
            print(rm_output.stderr.decode('utf-8'))
            raise Exception(f"Remove failed: {path}")



if __name__ == "__main__":
    CreateBinary()