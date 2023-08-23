# rest-framework-redesign

Redesign of the browsable API of Django REST Framework using Bootstrap 5.

The project aims to improve the look and feel of the API. Starting from version 0.2.2, the project supports dark mode.

## Get started

Install the package:

```bash
pip install rest-framework-redesign
```

Add `rest_framework_redesign` to `INSTALLED_APPS` setting, make sure that it's before `rest_framework`

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework_redesign',
    'rest_framework',
    ...
]
```

Include `rest_framework.urls` in your project URLConf

```python
# urls.py

...
from django.urls import path, include

urlpatterns = [
    ...
    path('auth/', include('rest_framework.urls')),
    ...
]
```

I hope you find this useful.
