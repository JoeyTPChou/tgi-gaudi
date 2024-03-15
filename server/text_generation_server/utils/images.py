import base64
from io import BytesIO
from PIL import Image


def b64_encode(image: Image.Image, format: str = "JPEG") -> str:
    im_file = BytesIO()
    image.save(im_file, format=format)
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    return base64.b64encode(im_bytes)


def b64_decode(b64: str) -> Image.Image:
    im_bytes = base64.b64decode(b64)  # im_bytes is a binary image
    im_file = BytesIO(im_bytes)  # convert image to file-like object
    return Image.open(im_file)  # img is now PIL Image object
