import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
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


#Next, log in to the server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("opendoorsofficialnumber1@gmail.com", "bestdoors123")

msg = MIMEMultipart()
msg['Subject'] = 'subject'
msg['From'] = 'opendoorsofficialnumber1@gmail.com'
msg['To'] = 'saul.rubio@digitalonus.com'
msg['Subject'] = "OPEN DOORS CODE"

img_data = open("myqr.svg", 'rb').read()
image = MIMEImage(img_data, name="QR.svg", _subtype='svg')
msg.attach(image)

server.sendmail('Open Doors','saul.rubio@digitalonus.com', msg.as_string())
server.quit()
