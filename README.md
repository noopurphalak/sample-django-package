## Quick start

1. Run `pip install -e git+https://github.com/noopurphalak/sample-django-package#egg=sample-django-package` in your virtualenv for your Django Project.

2. Add "sample" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
   ...
   'sample',
   ]

3. Include the sample URLconf in your project urls.py like this::

   path('', include('sample.urls')),

4. Run `python manage.py migrate` to create the sample models.

5. Visit http://127.0.0.1:8000/ to get the sample JSON response `{"greeting": "Hello World"}`.
