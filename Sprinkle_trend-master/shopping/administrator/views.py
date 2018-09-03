from django.shortcuts import render,redirect
from main.models import *
from django.http import HttpResponse
from main.forms import *

# Create your views here.
def AdminLogin(request):
	if(request.method=='GET'):
		return render(request,'administrator/adminLogin.html',None)
	else:
		id=request.POST.get('loginid')
		Password=request.POST.get('password')
		try:
			u=Login.objects.get(email=id)
			if(u.password==Password):
				r=redirect('/adminHome/')
				return r
			else:
				msg='incorrect password'
				return render(request,'administrator/adminLogin.html',{'msg':msg})
		except:
			msg='incorrect username'
			return render(request,'administrator/adminLogin.html',{'msg':msg})

def AdminHome(request):
		users=Product.objects.values()
		data={'users':users}
		return render(request,'administrator/adminHome.html',None)

def AddCategory(request):
	if(request.method=='GET'):		
		form=CategoryForm()
		data={'form':form}
		return render(request,'administrator/addcategory.html',data)
	else:
		form=CategoryForm(request.POST)
		form.save()
		return redirect('/admin/categories/')

def AddBrand(request):
	if(request.method=='GET'):
		form=BrandForm()
		data={'form':form}
		return render(request,'administrator/addbrand.html',data)
	else:
		form=BrandForm(request.POST)
		form.save()
		return redirect('/admin/brands/')

def AddProduct(request):
	if(request.method=='GET'):
		form=ProductForm()
		data={'form':form}
		return render(request,'administrator/addproduct.html',data)
	else:
		form=ProductForm(request.POST)
		form.save()
		return redirect('/admin/products/')

		
def DeleteCategory(request,id):
	category=Category.objects.get(id=id)
	category.delete()
	return redirect('/admin/categories/')

def DeleteBrand(request,id):
	brand=Brand.objects.get(id=id)
	brand.delete()
	return redirect('/admin/brands/')

def DeleteProduct(request,id):
	product=Product.objects.get(id=id)
	product.delete()
	return redirect('/admin/products/')

def UpdateCategory(request,id):
	if(request.method=='GET'):
		category=Category.objects.get(id=id)
		formdata={'parentid':category.parentid,'name':category.name,'description':category.description}
		form=CategoryForm(formdata)
		data={'form':form}
		return render(request,'administrator/addcategory.html',data)
	else:
		category=Category.objects.get(id=id)
		form=CategoryForm(request.POST, instance=category)
		form.save()
		return redirect('/admin/categories/')

def UpdateBrand(request,id):
	if(request.method=='GET'):
		brand=Brand.objects.get(id=id)
		formdata={'name':brand.name,'logo':brand.logo}
		form=BrandForm(formdata)
		data={'form':form}
		return render(request,'administrator/addbrand.html',data)
	else:
		brand=Brand.objects.get(id=id)
		form=BrandForm(request.POST,instance=brand)
		form.save()
		return redirect('/admin/brands/')

def UpdateProduct(request,id):
	if(request.method=='GET'):
		product=Product.objects.get(id=id)
		formdata={'name':product.name,'price':product.price,'stock':product.stock,'brandid_id':product.brandid_id,'categoryid_id':product.categoryid_id,'sellerid_id':product.sellerid_id}
		form=ProductForm(formdata)
		data={'form':form}
		return render(request,'administrator/addproduct.html',data)
	else:
		product=Product.objects.get(id=id)
		form=ProductForm(request.POST,instance=product)
		form.save()
		return redirect('/admin/products/')

def Categories(request):
	categories=Category.objects.filter()
	data={'categories':categories}
	return render(request,'administrator/categories.html',data)

def Brands(request):
	brands=Brand.objects.filter()
	data={'brand':brands}
	return render(request,'administrator/brands.html',data)

def Products(request):
	products=Product.objects.filter()
	data={'product':products}
	return render(request,'administrator/products.html',data)


# Create your views here.
def login(request):
	if(request.method=='GET'):
		return render(request,'administrator/adminLogin.html',None)
	else:
		id=request.POST.get('loginid')
		Password=request.POST.get('password')
		try:
			u=Login.objects.get(email=id)
			if(u.password==Password):
				r=redirect('adminHome.html')
				return r
			else:
				msg='incorrect password'
				return render(request,'administrator/adminLogin.html',{'msg':msg})
		except:
			msg='incorrect username'
			return render(request,'administrator/adminLogin.html',{'msg':msg})