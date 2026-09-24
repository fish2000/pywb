# -*- coding: utf-8 -*-
#
# dl_wabac_sw_js.py – Download that JavaScript from npm.org
#

import sys, os
from pywb.utils import download_wabac_sw

def main():
    download_wabac_sw()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(main())