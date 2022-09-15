from django.shortcuts import render, HttpResponse
from Mybooks.models import Book

# Create your views here.
def index(request):
    return render(request, "index.html")



    
        
   