from django.db import models

# Create your models here.
class Login(models.Model):
	email=models.EmailField(max_length=100)
	password=models.SlugField(max_length=30)
	type=models.CharField(max_length=10)
	isactive=models.BooleanField(max_length=10)

class Seller(models.Model):
	contactname=models.CharField(max_length=20)
	businessname=models.CharField(max_length=20)
	phone1=models.CharField(max_length=13)
	phone2=models.CharField(max_length=13)
	email=models.EmailField(max_length=100)
	address=models.CharField(max_length=40)
	gstin=models.IntegerField()


class Customer(models.Model):
	loginid=models.CharField(max_length=100)
	password=models.SlugField(max_length=30)
	name=models.CharField(max_length=20)
	gender=models.CharField(max_length=10)
	phone=models.CharField(max_length=13)
	

class ShippingAddress(models.Model):
	customerid=models.ForeignKey(Login,on_delete=models.PROTECT)
	title=models.CharField(max_length=20)
	hno=models.CharField(max_length=20)
	area=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	pin=models.IntegerField()
	landmark=models.CharField(max_length=100)

class Brand(models.Model):
	name=models.CharField(max_length=30)
	logo=models.FileField()

class Category(models.Model):
	parentid=models.IntegerField()
	name=models.CharField(max_length=40)
	description=models.CharField(max_length=100)

class Product(models.Model):
	categoryid=models.ForeignKey(Category,on_delete=models.PROTECT)
	brandid=models.ForeignKey(Brand,on_delete=models.PROTECT)
	sellerid=models.ForeignKey(Seller,on_delete=models.PROTECT)
	name=models.CharField(max_length=50)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	stock=models.IntegerField()

class FeatureLookup(models.Model):
	categoryid=models.ForeignKey(Category,on_delete=models.PROTECT)
	name=models.CharField(max_length=50)

class FeatureValue(models.Model):
	productid=models.ForeignKey(Product,on_delete=models.PROTECT)
	featureid=models.ForeignKey(FeatureLookup,on_delete=models.PROTECT)
	value=models.CharField(max_length=40)

class Cart(models.Model):
	customerid=models.ForeignKey(Login,on_delete=models.PROTECT)
	productid=models.ForeignKey(Product,on_delete=models.PROTECT)

class Order(models.Model):
	customerid=models.ForeignKey(Login,on_delete=models.PROTECT)
	addressid=models.ForeignKey(ShippingAddress,on_delete=models.PROTECT)
	datetime=models.DateTimeField()
	amount=models.DecimalField(max_digits=10,decimal_places=2)

class OrderItem(models.Model):
	orderid=models.ForeignKey(Order,on_delete=models.PROTECT)
	productid=models.ForeignKey(Product,on_delete=models.PROTECT)
	quantity=models.IntegerField()

class Shipping(models.Model):
	orderid=models.ForeignKey(Order,on_delete=models.PROTECT)
	status=models.CharField(max_length=20)
	datetime=models.DateTimeField()