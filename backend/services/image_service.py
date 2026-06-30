from io import BytesIO
from PIL import Image


def image_to_png(upload_file):
    image = Image.open(upload_file.file)

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer