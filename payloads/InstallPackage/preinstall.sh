#!/bin/sh
app_path="/Library/Application Support/Dortania/OpenCore Legacy Patcher.app"
launch_agent_path="/Library/LaunchAgents/com.dortania.opencore-legacy-patcher.auto-patch.plist"
if [ -d "$app_path" ]; then
    echo "Found OpenCore Legacy Patcher.app, removing…"
    /bin/rm -rf "$app_path"
fi

if [ -f "$launch_agent_path" ]; then
    echo "Found launch agent, removing…"
    /bin/rm -f "$launch_agent_path"
fi
