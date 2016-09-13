import json
from time import time

from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from .models import FibonacciSeries


def index(request):
	""" Renders the Index Page """
	
	template = 'index.html'
	return render(request, template)

def fibonacci(number):
	""" Function to calculate Fibonacci"""
	num1, num2 = 0, 1
	while number:
		num1, num2, number = num2, num1+num2, number-1
	return num1

def calculate_result(request):
	""" Calculates Nth Number of 
	Fibonacci Series """

	if request.method=='POST':
		nterms = int(request.POST['nterms'])
		value = 0
		computation_time = 0.0
		qs = FibonacciSeries.objects.filter(nterms=nterms).first()
		if qs:  # If number already in database, don't re-calculate
			response_data = {'nterms':nterms, 'value':qs.value, 'computation_time':qs.computation_time}
		else:
			t0 = time() # Start Time
			if nterms <=0 :
				raise ValueError('Please enter a Positive Number')
			else:
				value = fibonacci(nterms)
				computation_time = round(time()-t0, 4) # Final Computation Time

			# Make Entry to database
			FibonacciSeries.objects.create(
				nterms = nterms,
				value = value,
				computation_time = computation_time
				)

			print "Entry is created"
			response_data = {'nterms':nterms, 'value':value, 'computation_time':computation_time}

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
			)
	else:
		response_data = {'nterms':nterms, 'value':'Error Occured !', 'computation_time':'Error Occured !'} 

		return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

	
