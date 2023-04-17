# rest-framework-redesign

Redesign of the browsable api of Django REST Framework

## Get started

To get started with rest-framework-redesign:

- Install the package:

  ```bash
    pip install rest-framework-redesign
  ```

- Add `rest_framework_redesign` to `INSTALLED_APPS` setting, make sure that it's before `rest_framework`

  ```python
    # settings.py

    INSTALLED_APPS = [
        ...
        'rest_framework_redesign',
        'rest_framework',
        ...
    ]
  ```

- Include `rest_framework.urls` in your project URLConf

  ```python
    # urls.py

    ...
    from django.urls import path, include

    urlpatterns = [
        ...
        path('admin/', admin.site.urls),
        path('auth/', include('rest_framework.urls')),
        ...
    ]
  ```

- Run the server

I hope you that you find this useful.
