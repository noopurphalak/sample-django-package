from django.urls import path

from sample.views import hello

urlpatterns = [path("", hello, name="hello")]
