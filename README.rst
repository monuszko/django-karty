=====
karty
=====

Karty is a simple Django app to manage menu cards. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "karty" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'karty',
    ]

2. Include the karty URLconf in your project urls.py like this::

    url(r'^karty/', include('karty.urls')),

3. Run `python manage.py migrate` to create the karty models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a card (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/karty/ see menu cards.
