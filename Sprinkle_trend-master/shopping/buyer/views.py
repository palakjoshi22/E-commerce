from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.forms import *
from main.models import *


# Create your views here.
def login(request):
	if(request.method=='GET'):
		return render(request,'buyer/login.html',None)
	else:
		id=request.POST.get('loginid')
		Password=request.POST.get('password')
		try:
			u=Customer.objects.get(loginid=id)
			if(u.password==Password):
				r=redirect('/home/')
				r.set_cookie('login',id)
				return r
			else:
				msg='incorrect password'
				return render(request,'buyer/login.html',{'msg':msg})
		except:
			msg='incorrect username'
			return render(request,'buyer/login.html',{'msg':msg})

def register(request):

	if(request.method=='GET'):
		form=CustomerForm()
		data={'form':form}
		return render(request,'buyer/register.html',data)
	else:
		form=CustomerForm(request.POST)
		id=request.POST.get('loginid')
		form.save()
		r=redirect('/home/')
		r.set_cookie('login',id)
		return r
