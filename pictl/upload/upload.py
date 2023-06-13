"""Upload module"""

import boto3
from rich import print as rprint

from pictl.config import Config


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
    s3 = boto3.resource(
        "s3",
        endpoint_url=settings[group]["endpoint"],
        aws_access_key_id=settings[group]["key"],
        aws_secret_access_key=settings[group]["secret"],
    )
    with open(filename, "rb") as data:
        s3.Bucket(settings[group]["prefix"]).put_object(Key=filename, Body=data)
        get_link(settings, filename, group)


def get_link(settings: dict, filename: str, group: str):
    if settings[group]["prefix"] == "":
        url = f'{settings[group]["url"]}/{filename}'
    else:
        url = f'{settings[group]["url"]}/{settings[group]["prefix"]}/{filename}'
    rprint(
        f"Direct URL: {url}\n"
        f"Markdown: ![{filename}]({url})\n"
        f'HTML Code: <img src="{url}" alt="{filename}" />\n'
    )
