from django.urls import path
from.import views
urlpatterns=[
    path('store',views.store,name='store'),
    path('category/store/<slug:category_slug>/',views.store,name='products_by_category'),
    path('category/store/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    path('search/',views.search,name='search'),

]