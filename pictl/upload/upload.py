"""Upload module"""

import boto3
from rich import print as rprint

from pictl.config import Config
from pictl.utils import get_content_type, get_object_key


def upload(filename: str, group: str) -> None:
    """Upload the file to remote storage.

    \b
    FILENAME is the name of the file to upload.
    GROUP is the group in the config file you want to use.
    """
    settings = Config().read()
    if group not in settings:
        rprint(f"No group {group} in configuration file.")
        groups = list(settings.keys())
        if "basic" in groups:
            groups.remove("basic")
        rprint(f"Please choose one group from below:\n  {groups}")
    else:
        upload_s3(settings, filename, group)


def upload_s3(settings: dict, filename: str, group: str):
    resource = {
        "endpoint_url": settings[group]["endpoint"],
        "aws_access_key_id": settings[group]["key"],
        "aws_secret_access_key": settings[group]["secret"],
        "region_name": settings[group]["region"],
    }
    s3 = boto3.resource("s3", **resource)
    with open(filename, "rb") as data:
        content_type = get_content_type(filename)
        key = get_object_key(filename, settings[group]["prefix"])
        s3.Bucket(settings[group]["bucket"]).put_object(
            Key=key,
            Body=data,
            ContentType=content_type,
        )
        get_link(settings, filename, group)


def get_link(settings: dict, filename: str, group: str):
    key = get_object_key(filename, settings[group]["prefix"])
    url = f'{settings[group]["url"]}/{key}'
    filename = filename.split("/")[-1]
    print(
        f"Direct URL: {url}\n"
        f"Markdown: ![{filename}]({url})\n"
        f'HTML Code: <img src="{url}" alt="{filename}" />\n'
    )
