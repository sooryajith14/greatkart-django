from django.db import models
from django.urls import reverse
from app_shop.models import Category

# Create your models here.
class products(models.Model):
    product_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    description=models.TextField(max_length=255,blank=True)
    price=models.IntegerField(default=0)
    pro_image=models.ImageField(upload_to='photos/products',blank=True)
    stock=models.IntegerField(default=0)
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color',is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice=(
    ('color','color'),
    ('size','size'),

)

class Variation(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variation_category_choice)
    variation_value=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    craeted_date=models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value

