# Copyright (C) 2022, Mykola Grymalyuk
# Copyright (C) 2023 Jazzzny

import logging
import plistlib
import subprocess
import webbrowser

from pathlib import Path


from resources import utilities, global_settings, constants
from resources.sys_patch import sys_patch_detect
from resources.wx_gui import gui_entry


class AutomaticSysPatch:
    """
    Library of functions for launch agent, including automatic patching
    """

    def __init__(self, global_constants: constants.Constants):
        self.constants: constants.Constants = global_constants


    def start_auto_patch(self):
        """
        Initiates automatic patching

        Auto Patching's main purpose is to try and tell the user they're missing root patches
        New users may not realize OS updates remove our patches, so we try and run when nessasary

        Conditions for running:
            - Verify running GUI (TUI users can write their own scripts)
            - Verify the Snapshot Seal is intact (if not, assume user is running patches)
            - Verify this model needs patching (if not, assume user upgraded hardware and OpenCore Legacy Patcher was not removed)

        If all these tests pass, start Root Patcher

        """

        logging.info("- Starting Automatic Patching")
        if self.constants.wxpython_variant is False:
            logging.info("- Auto Patch option is not supported on TUI, please use GUI")
            return

        if utilities.check_seal() is True:
            logging.info("- Detected Snapshot seal intact, detecting patches")
            patches = sys_patch_detect.DetectRootPatch(self.constants.computer.real_model, self.constants).detect_patch_set()
            if not any(not patch.startswith("Settings") and not patch.startswith("Validation") and patches[patch] is True for patch in patches):
                patches = []
            if patches:
                logging.info("- Detected applicable patches, determining whether possible to patch")
                if patches["Validation: Patching Possible"] is False:
                    logging.info("- Cannot run patching")
                    return

                logging.info("- Determined patching is possible, checking for OpenCore Legacy Patcher updates")
                patch_string = ""
                for patch in patches:
                    if patches[patch] is True and not patch.startswith("Settings") and not patch.startswith("Validation"):
                        patch_string += f"- {patch}\n"

                logging.info("- Proceeding with patching")
                if self.constants.launcher_script is None:
                    args_string = f"'{self.constants.launcher_binary}' --gui_patch"
                else:
                    args_string = f"{self.constants.launcher_binary} {self.constants.launcher_script} --gui_patch"


                args = [
                    "osascript",
                    "-e",
                    f"""display dialog "OpenCore Legacy Patcher has detected you're running without Root Patches, and would like to install them.\n\nmacOS wipes all root patches during OS installs and updates, so they need to be reinstalled.\n\nFollowing Patches have been detected for your system: \n{patch_string}\nWould you like to apply these patches?" """
                    f'with icon POSIX file "{self.constants.app_icon_path}"',
                ]
                output = subprocess.run(
                    args,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                )
                if output.returncode == 0:
                    args = [
                        "osascript",
                        "-e",
                        f'''do shell script "{args_string}"'''
                        f' with prompt "OpenCore Legacy Patcher would like to patch your root volume"'
                        " with administrator privileges"
                        " without altering line endings"
                    ]
                    subprocess.run(
                        args,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT
                    )
                return
            else:
                logging.info("- No patches detected")
        else:
            logging.info("- Detected Snapshot seal not intact, skipping")

        if self._determine_if_versions_match():
            self._determine_if_boot_matches()

    def _onWebviewNav(self, event):
        url = event.GetURL()
        webbrowser.open(url)

    def _determine_if_versions_match(self):
        """
        Determine if the booted version of OpenCore Legacy Patcher matches the installed version

        ie. Installed app is 0.2.0, but EFI version is 0.1.0

        Returns:
            bool: True if versions match, False if not
        """

        logging.info("- Checking booted vs installed OpenCore Legacy Patcher Build")
        if self.constants.computer.oclp_version is None:
            logging.info("- Booted version not found")
            return True

        if self.constants.computer.oclp_version == self.constants.patcher_version:
            logging.info("- Versions match")
            return True

        if self.constants.special_build is True:
            # Version doesn't match and we're on a special build
            # Special builds don't have good ways to compare versions
            logging.info("- Special build detected, assuming installed is older")
            return False

        args = [
            "osascript",
            "-e",
            f"""display dialog "OpenCore Legacy Patcher has detected that you are booting {'a different' if self.constants.special_build else 'an outdated'} OpenCore build\n- Booted: {self.constants.computer.oclp_version}\n- Installed: {self.constants.patcher_version}\n\nWould you like to update the OpenCore bootloader?" """
            f'with icon POSIX file "{self.constants.app_icon_path}"',
        ]
        output = subprocess.run(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        if output.returncode == 0:
            logging.info("- Launching GUI's Build/Install menu")
            self.constants.start_build_install = True
            gui_entry.EntryPoint(self.constants).start(entry=gui_entry.SupportedEntryPoints.BUILD_OC)

        return False


    def _determine_if_boot_matches(self):
        """
        Determine if the boot drive matches the macOS drive
        ie. Booted from USB, but macOS is on internal disk

        Goal of this function is to determine whether the user
        is using a USB drive to Boot OpenCore but macOS does not
        reside on the same drive as the USB.

        If we determine them to be mismatched, notify the user
        and ask if they want to install to install to disk.
        """

        logging.info("- Determining if macOS drive matches boot drive")

        should_notify = global_settings.GlobalEnviromentSettings().read_property("AutoPatch_Notify_Mismatched_Disks")
        if should_notify is False:
            logging.info("- Skipping due to user preference")
            return
        if self.constants.host_is_hackintosh is True:
            logging.info("- Skipping due to hackintosh")
            return
        if not self.constants.booted_oc_disk:
            logging.info("- Failed to find disk OpenCore launched from")
            return

        root_disk = self.constants.booted_oc_disk.strip("disk")
        root_disk = f"disk{root_disk.split('s')[0]}"

        logging.info(f"  - Boot Drive: {self.constants.booted_oc_disk} ({root_disk})")
        macOS_disk = utilities.get_disk_path()
        logging.info(f"  - macOS Drive: {macOS_disk}")
        physical_stores = utilities.find_apfs_physical_volume(macOS_disk)
        logging.info(f"  - APFS Physical Stores: {physical_stores}")

        disk_match = False
        for disk in physical_stores:
            if root_disk in disk:
                logging.info(f"- Boot drive matches macOS drive ({disk})")
                disk_match = True
                break

        if disk_match is True:
            return

        # Check if OpenCore is on a USB drive
        logging.info("- Boot Drive does not match macOS drive, checking if OpenCore is on a USB drive")

        disk_info = plistlib.loads(subprocess.run(["diskutil", "info", "-plist", root_disk], stdout=subprocess.PIPE).stdout)
        try:
            if disk_info["Ejectable"] is False:
                logging.info("- Boot Disk is not removable, skipping prompt")
                return

            logging.info("- Boot Disk is ejectable, prompting user to install to internal")

            args = [
                "osascript",
                "-e",
                """display dialog "OpenCore Legacy Patcher has detected that you are booting OpenCore from an USB or External drive.\n\nIf you would like to boot your Mac normally without a USB drive plugged in, you can install OpenCore to the internal hard drive.\n\nWould you like to launch OpenCore Legacy Patcher and install to disk?" """
                f'with icon POSIX file "{self.constants.app_icon_path}"',
            ]
            output = subprocess.run(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            if output.returncode == 0:
                logging.info("- Launching GUI's Build/Install menu")
                self.constants.start_build_install = True
                gui_entry.EntryPoint(self.constants).start(entry=gui_entry.SupportedEntryPoints.BUILD_OC)

        except KeyError:
            logging.info("- Unable to determine if boot disk is removable, skipping prompt")


    def install_auto_patcher_launch_agent(self):
        """
        Install the Auto Patcher Launch Agent

        Installs the following:
            - OpenCore-Legacy-Patcher.app in /Library/Application Support/Dortania/
            - com.dortania.opencore-legacy-patcher.auto-patch.plist in /Library/LaunchAgents/

        See start_auto_patch() comments for more info
        """

        if self.constants.launcher_script is not None:
            logging.info("- Skipping Auto Patcher Launch Agent, not supported when running from source")
            return

        services = {
            self.constants.auto_patch_launch_agent_path:        "/Library/LaunchAgents/com.dortania.opencore-legacy-patcher.auto-patch.plist",
            self.constants.update_launch_daemon_path:           "/Library/LaunchDaemons/com.dortania.opencore-legacy-patcher.macos-update.plist",
            **({ self.constants.rsr_monitor_launch_daemon_path: "/Library/LaunchDaemons/com.dortania.opencore-legacy-patcher.rsr-monitor.plist" } if self._create_rsr_monitor_daemon() else {}),
        }

        for service in services:
            name = Path(service).name
            logging.info(f"- Installing {name}")
            if Path(services[service]).exists():
                logging.info(f"  - Existing service found, removing")
                utilities.process_status(utilities.elevated(["rm", services[service]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))
            # Create parent directories
            if not Path(services[service]).parent.exists():
                logging.info(f"  - Creating {Path(services[service]).parent} directory")
                utilities.process_status(utilities.elevated(["mkdir", "-p", Path(services[service]).parent], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))
            utilities.process_status(utilities.elevated(["cp", service, services[service]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))

            # Set the permissions on the service
            utilities.process_status(utilities.elevated(["chmod", "644", services[service]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))
            utilities.process_status(utilities.elevated(["chown", "root:wheel", services[service]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))

        if self.constants.launcher_binary.startswith("/Library/Application Support/Dortania/"):
            logging.info("- Skipping Patcher Install, already installed")
            return

        # Verify our binary isn't located in '/Library/Application Support/Dortania/'
        # As we'd simply be duplicating ourselves
        logging.info("- Installing Auto Patcher Launch Agent")

        if not Path("Library/Application Support/Dortania").exists():
            logging.info("- Creating /Library/Application Support/Dortania/")
            utilities.process_status(utilities.elevated(["mkdir", "-p", "/Library/Application Support/Dortania"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))

        logging.info("- Copying OpenCore Legacy Patcher to /Library/Application Support/Dortania/")
        if Path("/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app").exists():
            logging.info("- Deleting existing OpenCore Legacy Patcher")
            utilities.process_status(utilities.elevated(["rm", "-R", "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))

        # Strip everything after OpenCore-Legacy-Patcher.app
        path = str(self.constants.launcher_binary).split("/Contents/MacOS/OpenCore-Legacy-Patcher")[0]
        logging.info(f"- Copying {path} to /Library/Application Support/Dortania/")
        utilities.process_status(utilities.elevated(["ditto", path, "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))

        if not Path("/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app").exists():
            # Sometimes the binary the user launches may have a suffix
            # We'll want to rename it to OpenCore-Legacy-Patcher.app
            path = path.split("/")[-1]
            logging.info(f"- Renaming {path} to OpenCore-Legacy-Patcher.app")
            utilities.process_status(utilities.elevated(["mv", f"/Library/Application Support/Dortania/{path}", "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))

        subprocess.run(["xattr", "-cr", "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Making app alias
        # Simply an easy way for users to notice the app
        # If there's already an alias or exiting app, skip
        if not Path("/Applications/OpenCore-Legacy-Patcher.app").exists():
            logging.info("- Making app alias")
            utilities.process_status(utilities.elevated(["ln", "-s", "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app", "/Applications/OpenCore-Legacy-Patcher.app"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT))


    def _create_rsr_monitor_daemon(self) -> bool:
        # Get kext list in /Library/Extensions that have the 'GPUCompanionBundles' property
        # This is used to determine if we need to run the RSRMonitor
        logging.info("- Checking if RSRMonitor is needed")

        cryptex_path = f"/System/Volumes/Preboot/{utilities.get_preboot_uuid()}/cryptex1/current/OS.dmg"
        if not Path(cryptex_path).exists():
            logging.info("- No OS.dmg, skipping RSRMonitor")
            return False

        kexts = []
        for kext in Path("/Library/Extensions").glob("*.kext"):
            if not Path(f"{kext}/Contents/Info.plist").exists():
                continue
            try:
                kext_plist = plistlib.load(open(f"{kext}/Contents/Info.plist", "rb"))
            except Exception as e:
                logging.info(f"  - Failed to load plist for {kext.name}: {e}")
                continue
            if "GPUCompanionBundles" not in kext_plist:
                continue
            logging.info(f"  - Found kext with GPUCompanionBundles: {kext.name}")
            kexts.append(kext.name)

        # If we have no kexts, we don't need to run the RSRMonitor
        if not kexts:
            logging.info("- No kexts found with GPUCompanionBundles, skipping RSRMonitor")
            return False

        # Load the RSRMonitor plist
        rsr_monitor_plist = plistlib.load(open(self.constants.rsr_monitor_launch_daemon_path, "rb"))

        arguments = ["rm", "-Rfv"]
        arguments += [f"/Library/Extensions/{kext}" for kext in kexts]

        # Add the arguments to the RSRMonitor plist
        rsr_monitor_plist["ProgramArguments"] = arguments

        # Next add monitoring for '/System/Volumes/Preboot/{UUID}/cryptex1/OS.dmg'
        logging.info(f"  - Adding monitor: {cryptex_path}")
        rsr_monitor_plist["WatchPaths"] = [
            cryptex_path,
        ]

        # Write the RSRMonitor plist
        plistlib.dump(rsr_monitor_plist, Path(self.constants.rsr_monitor_launch_daemon_path).open("wb"))

        return True
