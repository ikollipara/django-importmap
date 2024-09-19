"""
importmap.py
Ian Kollipara <ian.kollipara@gmail.com>

Importmap Interface
"""

from collections import namedtuple
from pathlib import Path

_Package = namedtuple("Package", ["name", "version", "remote"])

_PACKAGES = []


def pin(name: str, version: str = "latest"):
    """Pin the given package name with the given version. """

    _PACKAGES.append(_Package(name=name, version=version, remote=True))

def pin_from_apps():
    """Pin the javascript files from the STATIC_SRC_DIR"""

    from django.apps import apps
    from django.conf import settings

    STATIC_SRC_DIR = getattr(settings, "STATIC_SRC_DIR", "static_src")

    for config in apps.get_app_configs():
        for p in Path(config.path).glob("*"):
            if p.is_dir() and p.name == STATIC_SRC_DIR:
                config_path = Path(config.path) / STATIC_SRC_DIR
                config_path.relative_to(settings.BASE_DIR)
                _PACKAGES.append(_Package(name=f"@app/{config.name.replace(".", "-").replace("_", "-").lower()}", version=f"{config_path.relative_to(settings.BASE_DIR)}", remote=False))
