"""
_engine.py
Ian Kollipara <ian.kollipara@gmail.com>

Importmap Engine
"""

import httpx
from django.conf import settings


class Engine:
    JSPM_URL = "https://api.jspm.io/generate"
    _map = None

    def __init__(self):
        if self._map is None:
            self._parse()

    @classmethod
    def _parse(cls):
        from .importmap import _PACKAGES

        remote_packages = [
            f"{pkg.name}@{pkg.version}" for pkg in _PACKAGES if pkg.remote
        ]

        response = httpx.post(
            cls.JSPM_URL,
            json={
                "install": remote_packages,
                "env": [
                    "browser",
                    ("production" if not settings.DEBUG else "development"),
                    "module",
                ],
            },
        )

        map = response.json()
        for pkg in (p_ for p_ in _PACKAGES if not p_.remote):
            map["map"]["imports"][
                pkg.name
            ] = pkg.version  # version is just the path to the folder

        cls._map = map

    @classmethod
    def importmap(cls):
        if cls._map is None:
            cls._parse()

        return cls._map
