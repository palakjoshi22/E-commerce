"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

#Importing Views
from main import views as main
from seller import views as seller
from buyer import views as buyer
from administrator import views as administrator

urlpatterns = [

path('adminLogin/',administrator.AdminLogin),
path('adminHome/',administrator.AdminHome),
path('admin/category/add/',administrator.AddCategory),
path('admin/brand/add/',administrator.AddBrand),
path('admin/product/add/',administrator.AddProduct),
path('admin/category/delete/<int:id>/',administrator.DeleteCategory),
path('admin/brand/delete/<int:id>/',administrator.DeleteBrand),
path('admin/product/delete/<int:id>/',administrator.DeleteProduct),
path('admin/brand/update/<int:id>/',administrator.UpdateBrand),
path('admin/category/update/<int:id>/',administrator.UpdateCategory),
path('admin/product/update/<int:id>/',administrator.UpdateProduct),
path('admin/categories/',administrator.Categories),
path('admin/brands/',administrator.Brands),
path('admin/products/',administrator.Products),

path('home/',main.home),

path('client/login/',buyer.login),
path('client/register/',buyer.register),
]

urlpatterns += static("/",document_root=settings.BASE_DIR)
