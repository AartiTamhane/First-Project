from django.contrib import admin
from .models import ProductModel,CategoryModel, Customer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Price','category','description','image']
admin.site.register(ProductModel,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cname']
admin.site.register(CategoryModel,CategoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email','password']

admin.site.register(Customer,CustomerAdmin)