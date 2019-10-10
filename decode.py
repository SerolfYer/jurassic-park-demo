import pyqrcode
from pyqrcode import QRCode
import qrtools

#Decode the png
qr = qrtools.QR()
qr.decode("myqr.svg")
u'does it work?'
print(qr.data)
u'SCIENCE'
