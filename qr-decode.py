# zbarimg never works for me, this works
# pip3 install pyzbar opencv-python
import cv2
from pyzbar.pyzbar import decode

img = cv2.imread('qr.png')

decoded = decode(img)
for qr in decoded:
    print("QR code:", qr.data.decode('utf-8'))
