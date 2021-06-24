from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def homepage(request):
    return render (request, 'homepage.html')

def products(request):
    return render(request, 'products.html')

def ppes(request):
    return render(request, 'ppes.html')

def disinfectants(request):
    return render(request, 'disinfectants.html')

def accessories(request):
    return render(request, 'accessories.html')

def reviews(request):
    return render(request, 'reviews.html')

def about(request):
    return render(request, 'about.html')

def queries(request):
   return render(request, 'queries.html')

def newPage(request):
    cus_name = request.POST.get("name")
    cus_email = request.POST.get("email")
    cus_phone = request.POST.get("phone")
    cus_query = request.POST.get("query")

    o_ref = Post(name=cus_name, email=cus_email, phone=cus_phone, query=cus_query)
    o_ref.save()
    return render(request, 'queries.html', {"message":"registered!"})