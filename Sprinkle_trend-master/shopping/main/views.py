from django.shortcuts import render
from django.http import HttpResponse
from main.forms import *
from main.models import *

# Create your views here.

def user_login(request):
	form=Loginform()
	#users=Login.objects.values()
	return render(request,"login.html",{'form':form})

def home(request):
	brands=Brand.objects.filter()
	
	try:
		id=request.COOKIES.get('login')
		name=Customer.objects.get(loginid=id)
		data={'brand':brands,'name':name}
		return render(request,"main/home.html",data)
	except:
		name='no name'
		data={'brand':brands,'name':name}
		return render(request,"main/home.html",data)



