"""
importmap_tags.py
Ian Kollipara <ian.kollipara@gmail.com>

Importmap Tags
"""

import json

from django import template
from django.utils.safestring import mark_safe

from .._engine import Engine

register = template.Library()


@register.simple_tag()
@mark_safe
def importmap():
    return f'<script type="importmap">{json.dumps(Engine.importmap())}</script>'
