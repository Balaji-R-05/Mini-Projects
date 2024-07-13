import qrcode as qr

website = "https://www.google.com"
qr_code = qr.make(website)
qr_code.save("qrcode.png")
