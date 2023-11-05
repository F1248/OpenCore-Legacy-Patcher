# Generate UI for updating the patcher
import wx
import sys
import time
import logging
import datetime
import threading
import subprocess
import webbrowser

from pathlib import Path

from resources.wx_gui import gui_download, gui_support
from resources import constants, network_handler


class UpdateFrame(wx.Frame):
    """
    Create a frame for updating the patcher
    """
    def __init__(self, parent: wx.Frame, title: str, global_constants: constants.Constants, screen_location: wx.Point, url: str = "") -> None:
        logging.info("Initializing Update Frame")
        if parent:
            self.parent: wx.Frame = parent

            for child in self.parent.GetChildren():
                child.Hide()
            parent.Hide()
        else:
            super(UpdateFrame, self).__init__(parent, title=title, size=(350, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
            gui_support.GenerateMenubar(self, global_constants).generate()

        self.title: str = title
        self.constants: constants.Constants = global_constants
        self.application_path = self.constants.payload_path / "OpenCore-Legacy-Patcher.app"
        self.screen_location: wx.Point = screen_location
        if parent:
            self.parent.Centre()
            self.screen_location = parent.GetScreenPosition()
        else:
            self.Centre()
            self.screen_location = self.GetScreenPosition()


        self.url = url
        logging.info(f"Update URL: {url}")

        self.frame: wx.Frame = wx.Frame(
            parent=parent if parent else self,
            title=self.title,
            size=(512, 128),
            pos=self.screen_location,
            style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX
        )

        # Title: Preparing update
        title_label = wx.StaticText(self.frame, label="Preparing download…", pos=(-1,1))
        title_label.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))
        title_label.Centre(wx.HORIZONTAL)

        # Progress bar
        progress_bar = wx.Gauge(self.frame, range=100, pos=(10, 50), size=(300, 20))
        progress_bar.Centre(wx.HORIZONTAL)

        progress_bar_animation = gui_support.GaugePulseCallback(self.constants, progress_bar)
        progress_bar_animation.start_pulse()

        self.progress_bar = progress_bar
        self.progress_bar_animation = progress_bar_animation

        self.frame.Centre()
        self.frame.Show()
        wx.Yield()

        download_obj = None
        def _fetch_update() -> None:
            nonlocal download_obj
            download_obj = network_handler.DownloadObject(url, self.constants.payload_path / "OpenCore-Legacy-Patcher.app.zip")

        thread = threading.Thread(target=_fetch_update)
        thread.start()
        while thread.is_alive():
            wx.Yield()

        frame = gui_download.DownloadFrame(
            self.frame,
            title=self.title,
            global_constants=self.constants,
            download_obj=download_obj,
            item_name="OpenCore Legacy Patcher",
            download_icon=str(self.constants.app_icon_path)
        )

        if download_obj.download_complete is False:
            progress_bar_animation.stop_pulse()
            progress_bar.SetValue(0)
            if not frame.user_cancelled:
                message = wx.MessageDialog(self.frame, "Failed to download latest build. If you continue to experience this problem, please manually download OpenCore Legacy Patcher via your browser.", "Download failed!", wx.YES_NO | wx.ICON_ERROR | wx.NO_DEFAULT)
                message.SetYesNoLabels("Open in Browser", "Quit OpenCore Legacy Patcher")
                message.ShowModal()
                if message:
                    webbrowser.open(url)
            sys.exit(1)

        # Title: Extracting update…
        title_label.SetLabel("Extracting update…")
        title_label.Centre(wx.HORIZONTAL)
        wx.Yield()

        thread = threading.Thread(target=self._extract_update)
        thread.start()

        while thread.is_alive():
            wx.Yield()

        # Title: Installing update…
        title_label.SetLabel("Installing update…")
        title_label.Centre(wx.HORIZONTAL)

        thread = threading.Thread(target=self._install_update)
        thread.start()

        while thread.is_alive():
            wx.Yield()

        # Title: Update complete!
        title_label.SetLabel("Update complete!")
        title_label.Centre(wx.HORIZONTAL)

        # Progress bar
        progress_bar.Hide()
        progress_bar_animation.stop_pulse()

        # Label: Latest build has been installed to /Library/Application Support/Dortania!
        installed_label = wx.StaticText(self.frame, label="Latest build has been installed to /Library/Application Support/Dortania!", pos=(-1, progress_bar.GetPosition().y - 15))
        installed_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
        installed_label.Centre(wx.HORIZONTAL)

        # Label: Launching update shortly…
        launch_label = wx.StaticText(self.frame, label="Launching update shortly…", pos=(-1, installed_label.GetPosition().y + 30))
        launch_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        launch_label.Centre(wx.HORIZONTAL)

        # Adjust frame size
        self.frame.SetSize((-1, launch_label.GetPosition().y + 60))

        thread = threading.Thread(target=self._launch_update)
        thread.start()

        while thread.is_alive():
            wx.Yield()

        timer = 5
        while True:
            launch_label.SetLabel(f"Closing old process in {timer} seconds")
            launch_label.Centre(wx.HORIZONTAL)
            wx.Yield()
            time.sleep(1)
            timer -= 1
            if timer == 0:
                break

        sys.exit(0)


    def _extract_update(self) -> None:
        """
        Extracts the update
        """
        logging.info("Extracting update")
        if Path(self.application_path).exists():
            subprocess.run(["rm", "-rf", str(self.application_path)])

        # Some hell spawn at GitHub decided to double zip our GitHub Actions artifacts
        # So we need to unzip it twice
        for i in range(2):
            result = subprocess.run(["ditto", "-xk", str(self.constants.payload_path / "OpenCore-Legacy-Patcher.app.zip"), str(self.constants.payload_path)], capture_output=True)
            if result.returncode != 0:
                logging.error(f"Failed to extract update. Error: {result.stderr.decode('utf-8')}")
                wx.CallAfter(self.progress_bar_animation.stop_pulse)
                wx.CallAfter(self.progress_bar.SetValue, 0)
                wx.CallAfter(wx.MessageBox, f"Failed to extract update. Error: {result.stderr.decode('utf-8')}", "Extraction failed!", wx.OK | wx.ICON_ERROR)
                wx.CallAfter(sys.exit, 1)
                break

            if Path(self.application_path).exists():
                break

            if i == 1:
                logging.error("Failed to extract update. Error: Update file doesn't exist")
                wx.CallAfter(self.progress_bar_animation.stop_pulse)
                wx.CallAfter(self.progress_bar.SetValue, 0)
                wx.CallAfter(wx.MessageBox, "Failed to extract update. Error: Update file doesn't exist", "Extraction failed!", wx.OK | wx.ICON_ERROR)
                wx.CallAfter(sys.exit, 1)
                break


    def _install_update(self) -> None:
        """
        Installs update to '/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app'
        """
        logging.info(f"Installing update: {self.application_path}")

        # Create bash script to run as root
        script = f"""#!/bin/bash
# Check if '/Library/Application Support/Dortania' exists
if [ ! -d "/Library/Application Support/Dortania" ]; then
    mkdir -p "/Library/Application Support/Dortania"
fi

# Check if 'OpenCore-Legacy-Patcher.app' exists
if [ -d "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app" ]; then
    rm -rf "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app"
fi

if [ -d "/Applications/OpenCore-Legacy-Patcher.app" ]; then
    rm -rf "/Applications/OpenCore-Legacy-Patcher.app"
fi

# Move '/tmp/OpenCore-Legacy-Patcher.app' to '/Library/Application Support/Dortania'
mv "{str(self.application_path)}" "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app"

# Check if '/Applications/OpenCore-Legacy-Patcher.app' exists
ln -s "/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app" "/Applications/OpenCore-Legacy-Patcher.app"

# Create update.plist with info about update
cat << EOF > "/Library/Application Support/Dortania/update.plist"
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>InstallationDate</key>
    <date>{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}</date>
    <key>InstallationSource</key>
    <string>{self.url}</string>
</dict>
</plist>
EOF
"""
        # Write script to file
        with open(self.constants.payload_path / "update.sh", "w") as f:
            f.write(script)

        # Execute script
        args = [self.constants.oclp_helper_path, "/bin/sh", str(self.constants.payload_path / "update.sh")]
        result = subprocess.run(args, capture_output=True)
        if result.returncode != 0:
            wx.CallAfter(self.progress_bar_animation.stop_pulse)
            wx.CallAfter(self.progress_bar.SetValue, 0)
            if "User cancelled" in result.stderr.decode("utf-8"):
                logging.info("User cancelled update")
                wx.CallAfter(wx.MessageBox, "User cancelled update", "Update Cancelled", wx.OK | wx.ICON_INFORMATION)
            else:
                logging.warning(f"Failed to install update. Error: {result.stderr.decode('utf-8')}")
                wx.CallAfter(wx.MessageBox, f"Failed to install update. Error: {result.stderr.decode('utf-8')}", "Installation failed!", wx.OK | wx.ICON_ERROR)
            wx.CallAfter(sys.exit, 1)


    def _launch_update(self) -> None:
        """
        Launches newly installed update
        """
        logging.info("Launching update: '/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app'")
        subprocess.Popen(["/Library/Application Support/Dortania/OpenCore-Legacy-Patcher.app/Contents/MacOS/OpenCore-Legacy-Patcher", "--update_installed"])
