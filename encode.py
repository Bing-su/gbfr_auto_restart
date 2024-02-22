from base64 import b85encode
from pathlib import Path

from PIL import Image

root = Path(__file__).parent
image = root.joinpath("image")
data = root.joinpath("data.py")

with data.open("w", encoding="utf-8") as file:
    file.write("_images = {\n")
    for img in image.iterdir():
        try:
            _ = Image.open(img)
        except Exception:
            continue

        encoded = b85encode(img.read_bytes()).decode("utf-8")

        file.write(f'    "{img.stem}": "{encoded}",\n')
    file.write("}\n")
