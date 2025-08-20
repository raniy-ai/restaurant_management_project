from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'restuarant_name':'Tasty Bites'})
# Create your views here.
