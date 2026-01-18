import qrcode

url = "https://electrofarfanes.mx/eq1/AyV/Proyectito/login.html"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_url.png")

print("QR generado: qr_url.png")