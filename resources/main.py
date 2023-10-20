# Copyright (C) 2020-2022, Dhinak G, Mykola Grymalyuk

import os
import sys
import time
import logging
import threading
from pathlib import Path

from resources.wx_gui import gui_entry
from resources import (
    constants,
    utilities,
    device_probe,
    os_probe,
    defaults,
    arguments,
    reroute_payloads,
    commit_info,
    logging_handler,
    analytics_handler
)


class OpenCoreLegacyPatcher:
    """
    Initial entry point for starting OpenCore Legacy Patcher
    """

    def __init__(self) -> None:
        self.constants: constants.Constants = constants.Constants()

        logging_handler.InitializeLoggingSupport(self.constants)

        self._generate_base_data()

        if utilities.check_cli_args() is None:
            gui_entry.EntryPoint(self.constants).start()


    def _generate_base_data(self) -> None:
        """
        Generate base data required for the patcher to run
        """

        self.constants.wxpython_variant: bool = True

        # Ensure we live after parent process dies (ie. LaunchAgent)
        os.setpgrp()

        # Generate OS data
        os_data = os_probe.OSProbe()
        self.constants.detected_os = os_data.detect_kernel_major()
        self.constants.detected_os_minor = os_data.detect_kernel_minor()
        self.constants.detected_os_build = os_data.detect_os_build()
        self.constants.detected_os_version = os_data.detect_os_version()

        # Generate computer data
        self.constants.computer = device_probe.Computer.probe()
        self.computer = self.constants.computer
        self.constants.booted_oc_disk = utilities.find_disk_off_uuid(utilities.clean_device_path(self.computer.opencore_path))
        if self.constants.computer.firmware_vendor:
            if self.constants.computer.firmware_vendor != "Apple":
                self.constants.host_is_hackintosh = True

        # Generate environment data
        self.constants.recovery_status = utilities.check_recovery()
        utilities.disable_cls()

        # Generate binary data
        launcher_script = None
        launcher_binary = sys.executable
        if "python" in launcher_binary:
            # We're running from source
            launcher_script =  __file__
            if "main.py" in launcher_script:
                launcher_script = launcher_script.replace("/resources/main.py", "/OpenCore-Patcher-GUI.command")
        self.constants.launcher_binary = launcher_binary
        self.constants.launcher_script = launcher_script

        # Initialize working directory
        self.constants.unpack_thread = threading.Thread(target=reroute_payloads.RoutePayloadDiskImage, args=(self.constants))
        self.constants.unpack_thread.start()

        # Generate commit info
        self.constants.commit_info = commit_info.ParseCommitInfo(self.constants.launcher_binary).generate_commit_info()
        branch = self.constants.commit_info[0]
        if " " in branch:
            branch = self.constants.fallback_branch
        self.constants.pkg_nightly_url = self.constants.pkg_nightly_url.replace("branch_placeholder", branch)

        # Generate defaults
        defaults.GenerateDefaults(self.computer.real_model, True, self.constants)
        threading.Thread(target=analytics_handler.Analytics(self.constants).send_analytics).start()

        if utilities.check_cli_args() is None:
            self.constants.cli_mode = False
            return

        logging.info("Detected arguments, switching to CLI mode")
        self.constants.gui_mode = True  # Assumes no user interaction is required

        ignore_args = ["--auto_patch", "--gui_patch", "--gui_unpatch", "--update_installed"]
        if not any(x in sys.argv for x in ignore_args):
            self.constants.current_path = Path.cwd()
        ignore_args = ignore_args.pop(0)

        if not any(x in sys.argv for x in ignore_args):
            while self.constants.unpack_thread.is_alive():
                time.sleep(0.1)

        arguments.arguments(self.constants)
