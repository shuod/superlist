from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home_page(request):
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    return render(request, 'home.html')
