from django.test import TestCase
from django.utils import timezone
from fibonacci.models import FibonacciSeries
from fibonacci.forms import FibonacciSeriesForm

class FibonacciTestCase(TestCase):

	def create_fibonacci_series(self, nterms=6, value=8, computation_time=0):
		return FibonacciSeries.objects.create(nterms=nterms, value=value, computation_time=computation_time, timestamp=timezone.now())

	# Views Test
	def test_index(self):
		resp = self.client.get('/fibonacci/')
		self.assertEqual(resp.status_code, 200)

	# Models Test
	def test_fibonacci_series_creation(self):
		w = self.create_fibonacci_series()
		self.assertTrue(isinstance(w, FibonacciSeries))
		self.assertEqual(w.__unicode__(), str(w.nterms))

	#Forms Test
	def test_valid_form(self):
		w = FibonacciSeries.objects.create(nterms=20, value=6765, computation_time=0.01)
		data = {'nterms': w.nterms,'value':w.value, 'computation_time':w.computation_time}
		form = FibonacciSeriesForm(data=data)
		self.assertTrue(form.is_valid())

