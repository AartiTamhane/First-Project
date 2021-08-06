from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductModel, CategoryModel

# Create your views here.
def index(request):
    products = None
    categories= CategoryModel.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = ProductModel.get_all_products_by_categoryid(categoryID)
    else:
        products = ProductModel.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories
    return render(request,'index.html',data)



def signup(request):
    return render (request, 'signup.html')