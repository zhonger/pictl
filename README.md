# pictl

A command line tool for Image Compression and Upload (ex. S3-type)

![PyPI](https://img.shields.io/pypi/v/pictl)
![GitHub](https://img.shields.io/github/license/zhonger/pictl)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/zhonger/pictl)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pictl)

![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/zhonger/pictl)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/zhonger/pictl/python-publish.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pictl)

Engligh | [中文简体](https://lisz.me/tech/project/pictl.html)

## Why a new project

When I publish blog articles, it's quite inefficient for me to prepare images.

Although there exist many good enough tools, like [uPic](https://github.com/gee1k/uPic), [PicGo](https://github.com/Molunerfinn/PicGo), and so on, they still cannot meet my need completely.

For me, these points are very necessary:

- All images should be compressed and transformed into `webp` format (less storage and loading time).
- All images can be uploaded to S3-like object storage with a unique short name.
- It should be very easy to use. It‘s better if no web UI or GUI. Command line first.
- (Optional) The customized watermark can be added into all images automatically.
- (Optional) All images can be resized into the defined default size automatically.
- (Optional) It defaults to read the image from the clipboard.

Actually uPic and PicGo can provide most of the above functions, but not so good in some points.

- They don't provide the transformation to `webp` format.
- They don't provide the support for Cloudflare R2 (though uPic paid version in appstore provides it).

It's quite time-consuming for me to write a plugin for PicGo or rewrite codes for uPic.

So why not write a new tool?

## The project name

Because it's designed for image helper in writing blog articles and using only with command line,
it's named PICTL, a short name for **Pi**cture **C**on**t**ro**l**.

## The architecture

Here is the architecture of this project.

It seems very similar to PicGo 😂, but it will be different.

![The architecture](https://github.com/zhonger/pictl/assets/12064158/4560bc88-c58e-4f35-8dd3-0ccc4ff36673)

## Installation

### From source

```bash
git clone https://github.com/zhonger/pictl
cd pictl
pip3 install .
```

### PIP

```bash
pip3 install pictl
```

### Brew

(~~**PS**: It will support in the next version.~~ Now it's supported in MacOS. Linux is not available yet.)

```bash
brew tap zhonger/pictl
brew install pictl
```

## Usage

### Config

The config file for PICTL is named `.pictlrc` with `toml` format. The config file is located at `~/.pictlrc`.

Until now PICTL supports:

| Name | `type` in config |
| :--: | :--: |
| Cloudflare R2 | `R2` |
| AWS S3 | `S3` |
| Tencent COS | `COS(Tencent)` |

#### Manually

```bash
[basic]
length = 6
ntype = "random"
algorithm = "sha1"

[blog]
type = "S3"
endpoint = "https://s3.ap-northeast-1.amazonaws.com"
bucket = "blog"
region = "ap-northeast-1"
prefix = "blog"
key = "this-is-a-long-key-for-s3"
secret = "this-is-a-long-secret-for-s3"
url = "https://i.lisz.me"
```

### Interactive way

```bash
╰─$ pictl config
Usage: pictl config [OPTIONS] COMMAND [ARGS]...

  Operations for the config file `~/.pictlrc`.

Options:
  -h, --help  Show this message and exit.

Commands:
  add     Add configs to the config file.
  delete  Delete config group from the config file.
  info    Check the configs.
  init    Initialize config file with default configs
```
