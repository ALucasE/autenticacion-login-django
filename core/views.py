from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    contexto = {}
    
    return render(request, 'core/index.html', contexto)

@login_required
def products(request):
    contexto = {}
    
    return render(request, 'core/products.html', contexto)