#!/usr/bin/env python
# Import QRCode from pyqrcode
import pyqrcode
import os
from pyqrcode import QRCode
import qrtools


# String which represent the QR code
s = os.environ.get('ROOT_TOKEN')
print(s)

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("myqr.svg", scale = 8)


qr = qrtools.QR()
qr.decode("myqr.svg")
u'does it work?'
print qr.data
u'SCIENCE'