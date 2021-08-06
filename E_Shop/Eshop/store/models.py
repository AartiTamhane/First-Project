from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    cname = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return CategoryModel.objects.all()

    def __str__(self):
        return f'{self.cname}'

class ProductModel(models.Model):
    Name = models.CharField(max_length=30)
    Price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default='',null=True,blank=True)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')

    @staticmethod
    def get_all_products():
        return ProductModel.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return ProductModel.objects.filter(category=category_id)
        else:
            return ProductModel.get_all_products()




class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

