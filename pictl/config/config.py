"""Configuration module"""

from dataclasses import dataclass
from pathlib import Path

import inquirer
import rtoml
from rich import print as rprint


@dataclass
class Basic:
    bucket: str
    key: str
    secret: str
    url: str


@dataclass
class S3(Basic):
    endpoint: str


@dataclass
class R2(Basic):
    account_id: str


class Config:
    """Read or set configurations"""

    def __init__(self):
        self.rc = f"{Path.home()}/.pictlrc"
        self.settings = {}
        # self.settings = self.read()

    def read(self):
        with open(self.rc, "r", encoding="utf-8") as f:
            settings = rtoml.loads(f.read())
        return settings

    def write(self, config):
        with open(self.rc, "w+", encoding="utf-8") as f:
            f.write(rtoml.dumps(config))

    def init(self):
        if Path(self.rc).exists():
            rprint(
                f"{self.rc} already exists.\n"
                f"Please add settings or change it manaully."
            )
        else:
            config = {
                "basic": {
                    "length": 6,
                    "ntype": "random",
                    "algorithm": "sha1",
                }
            }
            self.write(config)
            rprint(f"The settings has been initilized in {self.rc}.")

    def add(self):
        config = self.read()
        group = ""
        print("****** Please input these information ******")
        while group == "":
            group = input("Group Name (default 'blog'): ") or "blog"
            if group in config:
                rprint(f"{group} already exists. Please try others.")
                group = ""
        types = [
            inquirer.List(
                "type",
                message="Type",
                choices=["S3", "R2"],
            ),
        ]
        type_ = inquirer.prompt(types)["type"]
        if type_ == "S3":
            add_config = self.add_S3()
        elif type_ == "R2":
            add_config = self.add_R2()
        add_config["type"] = type_
        config[group] = add_config
        self.write(config)
        rprint(f"New group '{group}' has been saved in {self.rc}.")

    def add_S3(self):
        regions = [
            inquirer.List(
                "region",
                message="Region",
                choices=[
                    "us-east-1",
                    "us-east-2",
                    "us-west-1",
                    "us-west-2",
                    "af-south-1",
                    "ap-east-1",
                    "ap-south-2",
                    "ap-southeast-3",
                    "ap-southeast-4",
                    "ap-south-1",
                    "ap-south-2",
                    "ap-northeast-3",
                    "ap-northeast-2",
                    "ap-southeast-1",
                    "ap-southeast-2",
                    "ap-northeast-1",
                    "ca-central-1",
                    "cn-north-1",
                    "cn-northwest-1",
                    "eu-central-1",
                    "eu-west-1",
                    "eu-west-2",
                    "eu-south-1",
                    "eu-west-3",
                    "eu-north-1",
                    "eu-south-2",
                    "eu-central-2",
                    "sa-east-1",
                    "me-south-1",
                    "me-central-1",
                    "us-gov-east-1",
                    "us-gov-west-1",
                ],
            ),
        ]
        region = inquirer.prompt(regions)["region"]
        bucket = ""
        while bucket == "":
            bucket = input("Bucket Name: ")
        key = ""
        while key == "":
            key = input("Key: ")
        secret = ""
        while secret == "":
            secret = input("Secret: ")
        prefix = ""
        while prefix == "":
            prefix = input("Prefix: ")
        url = ""
        while url == "":
            url = input("Access Url: ")
        endpoint = f"https://s3.{region}.amazonaws.com"
        add_config = {
            "endpoint": endpoint,
            "bucket": bucket,
            "prefix": prefix,
            "key": key,
            "secret": secret,
            "url": url,
        }
        return add_config

    def add_R2(self):
        account_id = ""
        while account_id == "":
            account_id = input("Account ID: ")
        bucket = ""
        while bucket == "":
            bucket = input("Bucket Name: ")
        key = ""
        while key == "":
            key = input("Key: ")
        secret = ""
        while secret == "":
            secret = input("Secret: ")
        prefix = input("Prefix (Default is None): ")
        url = ""
        while url == "":
            url = input("Access Url (like `https://i.example.com`): ")
        add_config = {
            "endpoint": f"https://{account_id}.r2.cloudflarestorage.com/{bucket}",
            "bucket": bucket,
            "prefix": prefix,
            "key": key,
            "secret": secret,
            "url": url,
        }
        return add_config

    def delete(self, group: str = None):
        config = self.read()
        groups = list(config.keys())
        groups.remove("basic")
        if group is None:
            types = [
                inquirer.List(
                    "group",
                    message="Please select one group",
                    choices=groups,
                ),
            ]
            group = inquirer.prompt(types)["group"]
        if group not in groups:
            rprint(f"{group} doesn't exist. Please use one of {groups}.")
        else:
            del config[group]
            self.write(config)
            rprint(f"{group} has been deleted.")
