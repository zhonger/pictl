"""Pic module"""

from PIL import Image
from rich import print as rprint

from pictl.config import Config
from pictl.utils import get_name


def compress(filename: str):
    """Compress any image into `webp` image.

    FILENAME is the name of the file to compress.
    """
    settings = Config().read()
    optimize = settings["basic"].get("optimize", True)
    quality = settings["basic"].get("quality", 75)
    try:
        imgfile = Image.open(filename).convert("RGB")
        filename = f"{get_name(filename)}.webp"
        imgfile.save(filename, "webp", optimize=optimize, quality=quality)
        rprint(f"The output file is {filename}")
        return filename
    except FileNotFoundError:
        rprint(f"{filename} doesn't exsit. Please check it again.")
        return None
