#!/bin/zsh

echo "Install Dependencies…"

if [[ $1 == "--install_pip" ]]
then
    echo "Install pip packages…"
    pip3.12 install --upgrade --pre pip setuptools
    pip3.12 install https://files.pythonhosted.org/packages/d1/b2/fcedc8255ec42afee97f9e6f0145c734bbe104aac28300214593eb326f1d/charset_normalizer-3.3.2-cp312-cp312-macosx_10_9_universal2.whl # from https://pypi.org/project/charset-normalizer/#files
    pip3.12 install --upgrade --pre -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython
    pip3.12 install --upgrade --pre requests pyobjc pyinstaller packaging py_sip_xnu py-applescript
fi

if [[ $1 == "--install_packages" ]]
then
    echo "Install WhiteBox Packages…"
    curl -O http://s.sudre.free.fr/Software/files/Packages.dmg
    hdiutil attach Packages.dmg
    sudo installer -pkg /Volumes/Packages\ */Install\ Packages.pkg -target /
    hdiutil detach /Volumes/Packages\ * -force
    rm Packages.dmg
fi

echo "Dependencies installation completed"
