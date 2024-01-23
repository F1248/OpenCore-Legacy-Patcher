#!/bin/zsh

echo "Installing Dependencies…"

arguments=($@)
if [ ${#arguments[@]} -eq 0 ]; then
    arguments=("--pip" "--packages")
fi

for argument in $arguments; do
    case $argument in
        "--pip")
            echo "- Installing pip packages…"
            /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3.12 install --upgrade --pre pip setuptools
            /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3.12 install --upgrade https://files.pythonhosted.org/packages/d1/b2/fcedc8255ec42afee97f9e6f0145c734bbe104aac28300214593eb326f1d/charset_normalizer-3.3.2-cp312-cp312-macosx_10_9_universal2.whl # source: https://pypi.org/project/charset-normalizer/#files
            /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3.12 install --upgrade --pre -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython
            /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3.12 install --upgrade --pre requests pyobjc pyinstaller packaging py_sip_xnu py-applescript
            ;;
        "--packages")
            echo "- Installing WhiteBox Packages…"
            /usr/bin/curl --remote-name http://s.sudre.free.fr/Software/files/Packages.dmg
            /usr/bin/hdiutil attach Packages.dmg
            /usr/bin/sudo /usr/sbin/installer -pkg /Volumes/Packages\ */Install\ Packages.pkg -target /
            /usr/bin/hdiutil detach /Volumes/Packages\ * -force
            /bin/rm Packages.dmg
            ;;
        *)
            echo "Unknown argument: $argument"
            ;;
        esac
done

echo "Dependencies installation completed!"
