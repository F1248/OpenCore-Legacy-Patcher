#!/bin/zsh
find "$(dirname "$0")" -type d -name "__pycache__" -exec rm -r {} +
rm -f "$(dirname "$0")/payloads/update.sh"
