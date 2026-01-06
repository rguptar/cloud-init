# Copyright (C) 2012 Yahoo! Inc.
#
# Author: Joshua Harlow <harlowja@yahoo-inc.com>
#
# This file is part of cloud-init. See LICENSE file for license information.

try:
    from cloudinit import meson_versions  # type: ignore

    __VERSION__ = meson_versions.UPSTREAM_VERSION
    _DOWNSTREAM_VERSION = meson_versions.DOWNSTREAM_VERSION
except ImportError:
    # Use a PEP 440 compliant development version when meson_versions.py
    # is not available (e.g., running from source without meson build).
    # This avoids setuptools warnings about invalid version strings.
    __VERSION__ = "0.0.0.dev0"
    _DOWNSTREAM_VERSION = "@DOWNSTREAM_VERSION@"  # Optional for packagers


FEATURES = [
    # supports network config version 1
    "NETWORK_CONFIG_V1",
    # supports network config version 2 (netplan)
    "NETWORK_CONFIG_V2",
]


def version_string():
    """Extract a version string from cloud-init."""
    if _DOWNSTREAM_VERSION != "@DOWNSTREAM_VERSION@":
        return _DOWNSTREAM_VERSION
    return __VERSION__
