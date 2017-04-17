=====
karty
=====

Karty is a Django app to manage menu cards. 

Quick start
-----------

1. Add "karty" and "rest_framework" to your INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'karty.apps.KartyConfig',
    ]

2. Include the karty URLconf in your project urls.py like this::

    url(r'^karty/', include('karty.urls')),


3. To enable translations, add JavascriptCatalog to your project's urls.py::
    from django.views.i18n import JavaScriptCatalog
    ...

    url('^jsi18n/karty/$',
        JavaScriptCatalog.as_view(packages=['karty']),
        name='javascript-catalog'),


4. Configure rest framework pagination::
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
        }


5. Run `python manage.py migrate` to create the karty models.

6. (Optional) you may run `python manage.py create_sample_data` and
    `python manage_py destroy_app_data` to delete all the instances once done.

7. Start the development server and visit http://127.0.0.1:8000/admin/
   to create menu cards and dishes (you'll need the Admin app enabled).

8. Visit http://127.0.0.1:8000/karty/ see menu cards.
