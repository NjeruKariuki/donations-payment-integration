from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {

    }
    return render(request, 'payments/home.html', context)