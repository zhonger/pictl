"""Pic module"""

from PIL import Image
from rich import print as rprint

from pictl.config import Config
from pictl.utils import get_name


def compress(fi: str, fo: str = None):
    """Compress any image into `webp` image.

    FI is the name of the input file.
    FO is the name of the output file.
    """
    try:
        settings = Config().read()
        optimize = settings["basic"].get("optimize", True)
        quality = settings["basic"].get("quality", 75)
    except FileNotFoundError:
        optimize = True
        quality = 75

    try:
        imgfile = Image.open(fi).convert("RGB")
        if fo:
            filename = f"{fo}.webp"
        else:
            filename = f"{get_name(fi)}.webp"
        imgfile.save(filename, "webp", optimize=optimize, quality=quality)
        rprint(f"The output file is {filename}")
        return filename
    except FileNotFoundError:
        rprint(f"{fi} doesn't exsit. Please check it again.")
        return None
