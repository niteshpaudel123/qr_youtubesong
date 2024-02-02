import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=6)
qr.add_data("https://youtu.be/kWpGgMIbCzY?si=CUys_5foEHBLd4EX")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="green")
img.save("nitesh_song.png")