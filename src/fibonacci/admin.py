from django.contrib import admin

from .models import FibonacciSeries

class FibonacciSeriesModelAdmin(admin.ModelAdmin):
	class meta:
		model = FibonacciSeries

admin.site.register(FibonacciSeries, FibonacciSeriesModelAdmin)
