from django.shortcuts import render
from storeapp.models import products
# Create your views here.
def index(request):
    product=products.objects.all().filter(is_available=True)
    return render(request,'index.html',{'product':product})