from django.test import TestCase

from ._engine import Engine
from .importmap import _PACKAGES, _Package, pin, pin_from_apps
from .templatetags.importmap_tags import importmap

# Create your tests here.


class TestImportmap(TestCase):

    def test_engine(self):

        engine = Engine()

        importmap_ = engine.importmap()

        self.assertIn("map", importmap_)
        self.assertIn("imports", importmap_["map"])
        self.assertIn("react", ", ".join(importmap_["map"]["imports"]))

    def test_importmap_templatetag(self):

        result = importmap()

        self.assertIn("react", str(result))

    def test_pin(self):

        pin("vue")

        self.assertIn(_Package(name="vue", version="latest", remote=True), _PACKAGES)

    def test_pin_from_apps(self):

        global _PACKAGES

        _backup = [pkg for pkg in _PACKAGES]
        _PACKAGES.clear()

        pin_from_apps()

        self.assertEqual(len(_PACKAGES), 1)
        self.assertIn(
            _Package(name="@app/posts", version="posts/static_src", remote=False),
            _PACKAGES,
        )

        _PACKAGES = [pkg for pkg in _backup]
