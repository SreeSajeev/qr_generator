import qrcode
print(qrcode.__file__)  # This should print the path to the qrcode module if it's installed correctly

# Create an instance of the QRCode class
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used
    box_size=10,  # controls how many pixels each "box" of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

# Add data to the QR Code
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("youtube_qr.png")
