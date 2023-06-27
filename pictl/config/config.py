"""Configuration module"""

from dataclasses import dataclass
from pathlib import Path

import inquirer
import tomlkit
from rich import print as rprint

from .regions import regions


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

    def read(self):
        with open(self.rc, "r", encoding="utf-8") as f:
            settings = tomlkit.loads(f.read())
            self.settings = settings
        return settings

    def write(self, config):
        with open(self.rc, "w+", encoding="utf-8") as f:
            f.write(tomlkit.dumps(config))

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
                choices=["S3", "R2", "COS(Tencent)"],
            ),
        ]
        type_ = inquirer.prompt(types)["type"]
        add_config = self.add_S3(type_)
        config[group] = add_config
        self.write(config)
        print("********************************************")
        rprint(f"New group '{group}' has been saved in {self.rc}.")

    def add_S3(self, type_: str):
        regions_list = [
            inquirer.List(
                "region",
                message="Region",
                choices=regions[type_],
            ),
        ]
        region = inquirer.prompt(regions_list)["region"]
        endpoint = self.get_endpoint(type_, region)
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
            "type": type_,
            "endpoint": endpoint,
            "bucket": bucket,
            "region": region,
            "prefix": prefix,
            "key": key,
            "secret": secret,
            "url": url,
        }
        return add_config

    def get_endpoint(self, type_: str, region: str):
        if type_ == "S3":
            endpoint = f"https://s3.{region}.amazonaws.com"
        if type_ == "R2":
            account_id = ""
            while account_id == "":
                account_id = input("Account ID: ")
            endpoint = f"https://{account_id}.r2.cloudflarestorage.com"
        elif type_ == "COS(Tencent)":
            endpoint = f"https://cos.{region}.myqcloud.com"
        return endpoint

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
