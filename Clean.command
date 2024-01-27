#!/bin/zsh
location="$(/usr/bin/dirname "$0")"
echo "location: $location"

/usr/bin/find "$location" -name "__pycache__" -type d -exec rm -r {} +
/bin/rm -fr "$location/build"
/bin/rm -fr "$location/Build-Folder"
/bin/rm -fr "$location/dist"
/bin/rm -f  "$location/payloads/OpenCore-Legacy-Patcher.app.zip"
/bin/rm -f  "$location/payloads/update.sh"
/bin/rm -f  "$location/payloads.dmg"
/bin/rm -f  "$location/Universal%20Binaries.zip"

echo 'Successfully cleaned up!'
