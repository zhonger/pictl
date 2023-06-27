"""PICTL module"""

from pictl.config import Config
from pictl.pic import compress
from pictl.upload import get_link, upload, upload_s3
from pictl.utils import get_hash_name, get_name, get_random_name

__all__ = [
    "Config",
    "compress",
    "upload",
    "upload_s3",
    "get_link",
    "get_name",
    "get_random_name",
    "get_hash_name",
]
__version__ = "0.2.0"
