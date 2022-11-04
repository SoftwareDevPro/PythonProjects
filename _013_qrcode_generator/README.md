
# Generates a QR code

Simple program to generate a QR code from a user-provided string

To run:

```
pip install pyqrcode
python qrcode_generate.py <string> <base filename for images>
```

Example:

```
python ./qrcode_generate.py a_string_to_encode encoded_string
```

generates two QR code images in the directory:

encoded_string.png
encoded_string.svg
