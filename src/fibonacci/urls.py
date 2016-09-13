from django.conf.urls import url
from django.contrib import admin

from .views import (
	calculate_result,
	index
	)

urlpatterns = [
	url(r'^calculate/$', calculate_result, name='calculate_result'),
	url(r'^$', index, name='index'),
]