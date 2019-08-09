# Generates a .desktop file based on the current python version. Used for AUR installation
import os
import sys

desktop_file = """
[Desktop Entry]
Type = Application
Name = fpakman
Categories = System;
Comment = Manage your Flatpak / Snap applications
Exec = {path} --tray=1
Icon = {lib_path}/python{version}/site-packages/fpakman/resources/img/logo.svg
"""

py_version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)

with open('fpakman_tray.desktop', 'w+') as f:
    f.write(desktop_file.format(lib_path=os.getenv('FPAKMAN_LIB_PATH', '/usr/lib'),
                                version=py_version,
                                path=os.getenv('FPAKMAN_PATH', '/usr/bin/fpakman')))
