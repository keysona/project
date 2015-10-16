from django.conf.urls import include, url
from django.contrib import admin
from .views import test
from .views import upload
urlpatterns = [
        url(r'test/',test),
	url(r'upload/',upload)
	]
