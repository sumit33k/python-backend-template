from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

import simplejson as json

# Create your views here.

def test(request):
	result = dict(
			response="Connection successful",
		)
	return HttpResponse(json.dumps(result, indent=4))
