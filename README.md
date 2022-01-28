## Quick start

1. Add "sample" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
   ...
   'sample',
   ]

2. Include the sample URLconf in your project urls.py like this::

   path('', include('sample.urls')),

3. Run `python manage.py migrate` to create the sample models.

4. Visit http://127.0.0.1:8000/ to get the sample JSON response.
