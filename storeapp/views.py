from django.shortcuts import render, get_object_or_404
from app_shop.models import Category
from cart.models import cartitem
from cart.views import _cart_id
from .models import products
from django.core.paginator import Paginator
# Create your views here.
def store(request,category_slug=None):
    categories=None
    items=None

    if category_slug!=None:
        categories=get_object_or_404(Category,slug=category_slug)
        items=products.objects.filter(category=categories,is_available=True)
        paginator = Paginator(items, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        pro_count = items.count()
    else:
        items= products.objects.all().filter(is_available=True).order_by('id')
        paginator=Paginator(items,2)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        pro_count= items.count()

    context={
      "items":paged_products,
      "pro_count":pro_count,
    }
    return render(request,'store/store.html',context)
def product_details(request,category_slug,product_slug):
    single_product=products.objects.get(category__slug=category_slug,slug=product_slug)
    in_cart=cartitem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()

    return render(request,'store/product-detail.html',{'single_product':single_product,'in_cart':in_cart})

def search(request):
    return render(request,'store/store.html')