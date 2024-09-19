# Django Importmap

This is an implementation of Importmaps for Django.

## Usage

Add the application before all user application
```python
INSTALLED_APPS = [
    # ...,
    "django_importmaps",
    # ...,
]
```

Then define `importmap.py` at the top-level, with the following code:
```python
from django_importmaps import importmap

importmap.pin_from_apps()
```

Then to register a package add to `importmap.py`:
```python
importmap.pin("react")
```

Lastly, include the following templatetag:
```html
{% load importmap_tags %}

<html>
    <head>
        {% importmap %}
    </head>
    <body>
    </body>
</html>
```
