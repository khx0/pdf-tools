#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2017-07-20
# file: compress_pdf.py
# requires: ghostscript ($gs)
##########################################################################################

import time
import datetime
import sys
import os
import math
import numpy as np
import glob
import re

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR  = os.path.join(BASEDIR, 'raw')
OUTDIR  = os.path.join(BASEDIR, 'out')

if __name__ == '__main__':

    sourceFile = 'my_PDF_document.pdf
    targetFile = 'my_compressed_PDF_document.pdf'

    # PDF SETTINGS options:
    # -dPDFSETTINGS=/screen  -> 72 dpi
    # -dPDFSETTINGS=/ebook   -> 150 dpi
    # -dPDFSETTINGS=/printer -> 300 dpi

    cmd = 'gs -sDEVICE=pdfwrite ' + \
          '-dCompatibilityLevel=1.4 ' + \
          '-dPDFSETTINGS=/ebook ' + \
          '-dNOPAUSE ' + \
          '-dBATCH ' + \
          '-sOutputFile=%s %s' %(targetFile, sourceFile)

    os.system(cmd)
