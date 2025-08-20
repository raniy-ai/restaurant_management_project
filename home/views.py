from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'restuarant_name':'Tasty Bites'})
    'restuarant_phone':settings.RESTUARANT_PHONE,
    }
    return render(request, 'home.html',context)
# Create your views here.
