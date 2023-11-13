# Parse Build Arguments Info from binary's info.plist

from pathlib import Path
import plistlib
import time

class ParseBuildArguments:

    def __init__(self, binary_path: str) -> None:
        """
        Parameters:
            binary_path (str): Path to binary
        """

        self.binary_path = str(binary_path)
        self.plist_path = self._convert_binary_path_to_plist_path()


    def _convert_binary_path_to_plist_path(self) -> str or None:
        """
        Resolve Info.plist path from binary path
        """

        if Path(self.binary_path).exists():
            plist_path = self.binary_path.replace("MacOS/OpenCore-Legacy-Patcher", "Info.plist")
            if Path(plist_path).exists() and plist_path.endswith(".plist"):
                return plist_path
        return None


    def generate_build_arguments(self) -> dict:
        """
        Generate build arguments from Info.plist
        """

        if self.plist_path:
            plist_info = plistlib.load(Path(self.plist_path).open("rb"))
            return plist_info["Build arguments"]
        else:
            return None
