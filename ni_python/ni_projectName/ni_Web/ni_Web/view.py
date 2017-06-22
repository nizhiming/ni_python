
#from django.http import HttpResponse
from django.shortcuts import render

def ni_Web(request):
	context          = {}
	context['ni_hello'] = 'hello xiaominger'
	return render(request, 'ni_hello.html', context)
	#return HttpResponse("Welcome to xiaoming's room!")
