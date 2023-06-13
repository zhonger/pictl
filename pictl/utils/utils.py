"""Tools module"""

import hashlib
import random
import string

from pictl.config import Config


def get_name(filename: str):
    settings = Config().read()
    ntype = settings["basic"].get("ntype", None)
    length = settings["basic"].get("length", 8)
    algorithm = settings["basic"].get("algorithm", "sha1")
    if ntype == "random":
        name = get_random_name(length)
    elif ntype == "hash":
        name = get_hash_name(filename, algorithm, length)
    else:
        name = filename.split(".")[0]
    return name


def get_random_name(length: int = 8):
    name = "".join(
        random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase, k=length
        )
    )
    return name


def get_hash_name(filename: str, algorithm: str = "sha1", length: int = 8):
    with open(filename, "rb") as f:
        value = hashlib.new(algorithm, f.read()).hexdigest()
        name = value[:length].upper()
    return name
