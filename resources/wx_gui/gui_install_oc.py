import wx
import threading
import logging

from resources.wx_gui import gui_main_menu, gui_support
from resources import constants, install


class InstallOCFrame(wx.Frame):
    """
    Create a frame for installing OpenCore to disk
    """
    def __init__(self, parent: wx.Frame, title: str, global_constants: constants.Constants, screen_location: tuple = None):
        super(InstallOCFrame, self).__init__(parent, title=title, size=(300, 120))

        self.constants: constants.Constants = global_constants
        self.title: str = title
        self.result: bool = False

        self.available_disks: dict = None
        self.stock_output = logging.getLogger().handlers[0].stream

        self._generate_elements()

        self.SetPosition(screen_location) if screen_location else self.Centre()
        self.Show()

        self._display_disks()


    def _generate_elements(self) -> None:
        """
        Display indeterminate progress bar while collecting disk information

        Format:
            - Title label:        Install OpenCore
            - Text:               Fetching information on local disks...
            - Progress bar:       {indeterminate}
        """

        # Title label: Install OpenCore
        title_label = wx.StaticText(self, label="Install OpenCore", pos=(-1,5))
        title_label.SetFont(wx.Font(19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, ".AppleSystemUIFont"))
        title_label.Center(wx.HORIZONTAL)

        # Text: Parsing local disks...
        text_label = wx.StaticText(self, label="Fetching information on local disks...", pos=(-1,30))
        text_label.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, ".AppleSystemUIFont"))
        text_label.Center(wx.HORIZONTAL)
        self.text_label = text_label

        # Progress bar: {indeterminate}
        progress_bar = wx.Gauge(self, range=100, pos=(-1, text_label.GetPosition()[1] + text_label.GetSize()[1]), size=(150, 30), style=wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        progress_bar.Center(wx.HORIZONTAL)
        progress_bar.Pulse()
        self.progress_bar = progress_bar


    def _fetch_disks(self) -> None:
        """
        Fetch information on local disks
        """
        self.available_disks = install.tui_disk_installation(self.constants).list_disks()


    def _display_disks(self) -> None:
        """
        Display disk selection dialog
        """
        thread = threading.Thread(target=self._fetch_disks)
        thread.start()

        while thread.is_alive():
            wx.Yield()
            continue

        self.progress_bar.Hide()

        # Create wxDialog for disk selection
        dialog = wx.Dialog(self, title=self.title, size=(370, -1))

        # Title label: Install OpenCore
        title_label = wx.StaticText(dialog, label="Install OpenCore", pos=(-1,5))
        title_label.SetFont(wx.Font(19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, ".AppleSystemUIFont"))
        title_label.Center(wx.HORIZONTAL)

        # Text: select disk to install OpenCore onto
        text_label = wx.StaticText(dialog, label="Select disk to install OpenCore onto:", pos=(-1, title_label.GetPosition()[1] + title_label.GetSize()[1] + 5))
        text_label.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, ".AppleSystemUIFont"))
        text_label.Center(wx.HORIZONTAL)

        # Add note: "Missing disks? Ensure they're FAT32 or formatted as GUID/GPT"
        gpt_note = wx.StaticText(dialog, label="Missing disks? Ensure they're FAT32 or formatted as GUID/GPT", pos=(-1, text_label.GetPosition()[1] + text_label.GetSize()[1] + 5))
        gpt_note.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, ".AppleSystemUIFont"))
        gpt_note.Center(wx.HORIZONTAL)

        # Add buttons for each disk
        if self.available_disks is None:
            # Text: Failed to find any applicable disks
            disk_label = wx.StaticText(dialog, label="Failed to find any applicable disks", pos=(-1, gpt_note.GetPosition()[1] + gpt_note.GetSize()[1] + 5))
            disk_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, ".AppleSystemUIFont"))
            disk_label.Center(wx.HORIZONTAL)
        else:
            disk_root = self.constants.booted_oc_disk
            if disk_root:
                # disk6s1 -> disk6
                disk_root = self.constants.booted_oc_disk.strip("disk")
                disk_root = "disk" + disk_root.split("s")[0]

            # Add buttons for each disk
            for disk in self.available_disks:
                # Create a button for each disk
                logging.info(f"- {self.available_disks[disk]['disk']} - {self.available_disks[disk]['name']} - {self.available_disks[disk]['size']}")
                disk_button = wx.Button(dialog, label=f"{self.available_disks[disk]['disk']} - {self.available_disks[disk]['name']} - {self.available_disks[disk]['size']}", size=(300,30), pos=(-1, gpt_note.GetPosition()[1] + gpt_note.GetSize()[1] + 5))
                disk_button.Center(wx.HORIZONTAL)
                disk_button.Bind(wx.EVT_BUTTON, lambda event, disk=disk: self._display_volumes(disk, self.available_disks))
                if disk_root == self.available_disks[disk]['disk']:
                    disk_button.SetForegroundColour((25, 179, 231))


            if disk_root:
                # Add note: "Note: Blue represent the disk OpenCore is currently booted from"
                disk_label = wx.StaticText(dialog, label="Note: Blue represent the disk OpenCore is currently booted from", pos=(-1, disk_button.GetPosition()[1] + disk_button.GetSize()[1] + 5))
                disk_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, ".AppleSystemUIFont"))
                disk_label.Center(wx.HORIZONTAL)
            else:
                disk_label = wx.StaticText(dialog, label="", pos=(-1, disk_button.GetPosition()[1] + 15))
                disk_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, ".AppleSystemUIFont"))

        # Add button: Search for disks again
        search_button = wx.Button(dialog, label="Search for disks again", size=(200,30), pos=(-1, disk_label.GetPosition()[1] + disk_label.GetSize()[1] + 5))
        search_button.Center(wx.HORIZONTAL)
        search_button.Bind(wx.EVT_BUTTON, self._reload_frame)

        # Add button: Return to main menu
        return_button = wx.Button(dialog, label="Return to main menu", size=(200,30), pos=(-1, search_button.GetPosition()[1] + 25))
        return_button.Center(wx.HORIZONTAL)
        return_button.Bind(wx.EVT_BUTTON, self._return_to_main_menu)

        # Set size
        dialog.SetSize((370, return_button.GetPosition()[1] + return_button.GetSize()[1] + 40))
        dialog.ShowWindowModal()
        self.dialog = dialog


    def _display_volumes(self, disk: str, dataset: dict) -> None:
        """
        List volumes on disk
        """

        self.dialog.Close()

        # Create dialog
        dialog = wx.Dialog(
            self,
            title=f"Volumes on {disk}",
            style=wx.CAPTION | wx.CLOSE_BOX,
            size=(370, 300)
        )

        # Add text: "Volumes on {disk}"
        text_label = wx.StaticText(dialog, label=f"Volumes on {disk}", pos=(-1, 10))
        text_label.SetFont(wx.Font(19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, ".AppleSystemUIFont"))
        text_label.Center(wx.HORIZONTAL)

        partitions = install.tui_disk_installation(self.constants).list_partitions(disk, dataset)
        for partition in partitions:
            logging.info(f"- {partitions[partition]['partition']} - {partitions[partition]['name']} - {partitions[partition]['size']}")
            disk_button = wx.Button(dialog, label=f"{partitions[partition]['partition']} - {partitions[partition]['name']} - {partitions[partition]['size']}", size=(300,30), pos=(-1, text_label.GetPosition()[1] + text_label.GetSize()[1] + 5))
            disk_button.Center(wx.HORIZONTAL)
            disk_button.Bind(wx.EVT_BUTTON, lambda event, partition=partition: self._install_oc_process(partition))

        # Add button: Return to main menu
        return_button = wx.Button(dialog, label="Return to main menu", size=(200,30), pos=(-1, disk_button.GetPosition()[1] + disk_button.GetSize()[1]))
        return_button.Center(wx.HORIZONTAL)
        return_button.Bind(wx.EVT_BUTTON, self._return_to_main_menu)

        # Set size
        dialog.SetSize((370, return_button.GetPosition()[1] + return_button.GetSize()[1] + 40))

        # Show dialog
        dialog.ShowWindowModal()
        self.dialog = dialog


    def _install_oc_process(self, partition: dict) -> None:
        """
        Install OpenCore to disk
        """
        self.dialog.Close()

        # Create dialog
        dialog = wx.Dialog(
            self,
            title=f"Installing OpenCore to {partition}",
            style=wx.CAPTION | wx.CLOSE_BOX,
            size=(370, 200)
        )

        # Add text: "Installing OpenCore to {partition}"
        text_label = wx.StaticText(dialog, label=f"Installing OpenCore to {partition}", pos=(-1, 10))
        text_label.SetFont(wx.Font(19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, ".AppleSystemUIFont"))
        text_label.Center(wx.HORIZONTAL)

        # Read-only text box: {empty}
        text_box = wx.TextCtrl(dialog, value="", pos=(-1, text_label.GetPosition()[1] + text_label.GetSize()[1] + 10), size=(370, 200), style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_RICH2)
        text_box.Center(wx.HORIZONTAL)
        self.text_box = text_box

        # Add button: Return to main menu
        return_button = wx.Button(dialog, label="Return to main menu", size=(200,30), pos=(-1, text_box.GetPosition()[1] + text_box.GetSize()[1] + 10))
        return_button.Center(wx.HORIZONTAL)
        return_button.Bind(wx.EVT_BUTTON, self._return_to_main_menu)
        return_button.Disable()

        # Set size
        dialog.SetSize((370, return_button.GetPosition()[1] + return_button.GetSize()[1] + 40))

        # Show dialog
        dialog.ShowWindowModal()
        self.dialog = dialog

        # Install OpenCore
        self._invoke_install_oc(partition)
        return_button.Enable()


    def _invoke_install_oc(self, partition: dict) -> None:
        thread = threading.Thread(target=self._install_oc, args=(partition,))
        thread.start()

        while thread.is_alive():
            # wx.Yield()
            wx.GetApp().Yield()

        if self.result is True:
            if not self.constants.custom_model:
                gui_support.RestartHost(self).restart(message="OpenCore has finished installing to disk.\n\nYou will need to reboot and hold the Option key and select OpenCore/Boot EFI's option.\n\nWould you like to reboot?")
            else:
                popup_message = wx.MessageDialog(
                    self,
                    f"OpenCore has finished installing to disk.\n\nYou can eject the drive, insert it into the {self.constants.custom_model}, reboot, hold the Option key and select OpenCore/Boot EFI's option.", "Success",
                    wx.OK
                )
                popup_message.ShowModal()


    def _install_oc(self, partition: dict) -> None:
        """
        Install OpenCore to disk
        """
        logging.info(f"- Installing OpenCore to {partition}")

        logger = logging.getLogger()
        logger.addHandler(gui_support.ThreadHandler(self.text_box))
        self.result = install.tui_disk_installation(self.constants).install_opencore(partition)
        logger.removeHandler(logger.handlers[2])


    def _reload_frame(self, event) -> None:
        """
        Reload frame
        """
        self.Destroy()
        frame = InstallOCFrame(
            None,
            title=self.title,
            global_constants=self.constants,
            screen_location=self.GetScreenPosition()
        )
        frame.Show()


    def _return_to_main_menu(self, event: wx.Event) -> None:
        """
        Return to main menu
        """
        main_menu_frame = gui_main_menu.MainMenu(
            None,
            title=self.title,
            global_constants=self.constants,
            screen_location=self.GetScreenPosition()
        )
        main_menu_frame.Show()
        self.Destroy()




