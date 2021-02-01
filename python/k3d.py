#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pathlib import Path

import click

from click_project.decorators import (
    argument,
    flag,
    option,
    group,
    use_settings,
    table_format,
    table_fields,
)
from click_project.lib import (
    TablePrinter,
    call,
    move,
    download,
    extract,
    tempdir,
)
from click_project.config import config
from click_project.log import get_logger
from click_project.types import DynamicChoice


LOGGER = get_logger(__name__)


@group()
def k3d():
    """Manipulate k3d"""


bindir = Path("~/.local/bin").expanduser()
k3d_url = "https://github.com/rancher/k3d/releases/download/v4.0.0/k3d-linux-amd64"
helm_url = "https://get.helm.sh/helm-v3.5.0-linux-amd64.tar.gz"
kubectl_url = "https://dl.k8s.io/release/v1.20.2/bin/linux/amd64/kubectl"


@k3d.command()
def install_dependencies():
    """Install the dependencies needed to setup the stack"""
    download(k3d_url, outdir=bindir, outfilename="k3d", mode=0o755)
    with tempdir() as d:
        extract(helm_url, d)
        move(Path(d) / "linux-amd64" / "helm", bindir / "helm")
        (bindir / "helm").chmod(0o755)
    download(kubectl_url, outdir=bindir, outfilename="kubectl", mode=0o755)


@k3d.command()
def install_local_registry():
    """Run """
