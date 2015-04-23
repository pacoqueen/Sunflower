#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""From
http://askubuntu.com/questions/5172/running-a-desktop-file-in-the-terminal"""

from gi.repository import Gio
import sys 

def main(myname, desktop, *uris):
    launcher = Gio.DesktopAppInfo.new_from_filename(desktop)
    launcher.launch_uris(uris, None)

if __name__ == "__main__":
    main(*sys.argv)
