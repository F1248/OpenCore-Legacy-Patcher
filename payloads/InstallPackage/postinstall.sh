#!/bin/sh

# Create alias for OpenCore Legacy Patcher.app
if [ ! -d "/Applications/OpenCore Legacy Patcher.app" ]; then
    /bin/ln -s "/Library/Application Support/Dortania/OpenCore Legacy Patcher.app" "/Applications/OpenCore Legacy Patcher.app"
fi

# Start root patching
"/Library/Application Support/Dortania/OpenCore Legacy Patcher.app/Contents/MacOS/OpenCore-Legacy-Patcher" "--patch_sys_vol" &> "/Users/Shared/.OCLP-AutoPatcher-Log-$(/bin/date +"%Y_%m_%d_%I_%M_%p").txt"
/usr/bin/log show --last boot > "/Users/Shared/.OCLP-System-Log-$(/bin/date +"%Y_%m_%d_%I_%M_%p").txt"
/sbin/reboot
