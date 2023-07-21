from django.contrib import admin

from storeapp.models import products, Variation

# Register your models here.


class VariationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active')
    list_editable=('is_active',)
    list_filter=('product','variation_category','variation_value',)
admin.site.register(products)
admin.site.register(Variation,VariationAdmin)