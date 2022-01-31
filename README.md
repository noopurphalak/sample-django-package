## Quick start

1. Run the following command in your virtualenv for your Django Project:

   ```bash
   pip install -e git+https://github.com/noopurphalak/sample-django-package#egg=sample-django-package
   ```

2. Add "sample" to your INSTALLED_APPS setting like this:

   ```python
   INSTALLED_APPS = [
   ...
   'sample',
   ]
   ```

3. Include the sample URLconf in your project urls.py like this:

   ```python
   path('', include('sample.urls')),
   ```

4. Run `python manage.py migrate` to create the sample models (optional, models not added in the code yet).

5. Start the development server and visit http://127.0.0.1:8000/ to get the sample JSON response `{"greeting": "Hello World"}`.
