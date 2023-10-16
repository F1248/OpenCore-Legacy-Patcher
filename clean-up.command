#!/bin/zsh
location="$(dirname "$0")"
echo "location: $location"
find "$location" -name "__pycache__" -exec rm -r {} +
rm -f "$location/payloads/update.sh"
rm -f "$location/payloads.dmg"
rm -fr "$location/build"
rm -fr "$location/dist"

echo 'Successfully cleaned up!'