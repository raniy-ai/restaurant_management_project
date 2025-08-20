from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'restuarant_name':'Tasty Bites'})
    'restuarant_phone':settings.RESTUARANT_PHONE,
    }
    return render(request, 'home.html',context)
# Create your views here.

def menu_view(request):

    menu_items=[
        {"name":"Margherita Pizza", "price":250},
        {"name":"Pasta Alfredo","price":300 },
        {"name":"Veg Burger","price":150},
        {"name":"French Fires","prices"100},
    ]
    return render(request, "menu.html",{"menu_items":menu_items})
