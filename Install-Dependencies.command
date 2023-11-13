#!/bin/zsh

echo "Install Dependencies…"

echo "Install pip packages…"
pip3.11 install --upgrade --pre pip setuptools
pip3.11 install https://files.pythonhosted.org/packages/68/77/02839016f6fbbf808e8b38601df6e0e66c17bbab76dff4613f7511413597/charset_normalizer-3.3.2-cp311-cp311-macosx_10_9_universal2.whl # from https://pypi.org/project/charset-normalizer/#files
pip3.11 install --upgrade --pre requests pyobjc wxpython pyinstaller packaging py_sip_xnu py-applescript

echo "Install WhiteBox Packages…"
curl -O http://s.sudre.free.fr/Software/files/Packages.dmg
hdiutil attach Packages.dmg
sudo installer -pkg /Volumes/Packages\ */Install\ Packages.pkg -target /
hdiutil detach /Volumes/Packages\ * -force

echo "Dependencies installation completed"
