#!/bin/zsh
location="$(dirname "$0")"
echo "location: $location"

find "$location" -name "__pycache__" -exec rm -r {} +
rm -fr "$location/build"
rm -fr "$location/dist"
rm -f  "$location/payloads/OpenCore-Legacy-Patcher.app.zip"
rm -f  "$location/payloads/update.sh"
rm -f  "$location/payloads.dmg"

echo 'Successfully cleaned up!'