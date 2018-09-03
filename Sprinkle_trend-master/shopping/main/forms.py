from django.forms import ModelForm
from django import forms

from main.models import *

# Create your forms here.
class LoginForm(ModelForm):
	class Meta:
		model= Login
		fields= '__all__'

class SellerForm(ModelForm):
	class Meta:
		model= Seller
		fields= '__all__'

class CustomerForm(ModelForm):
	class Meta:
		model= Customer
		fields= '__all__'

class ShippingAddressForm(ModelForm):
	class Meta:
		model= ShippingAddress
		fields= '__all__'


class BrandForm(ModelForm):
	class Meta:
		model=Brand
		fields='__all__'

class CategoryForm(ModelForm):
	categories=Category.objects.filter()
	choices=[(0,'None')]

	for category in categories:
		c=(category.id,category.name)
		choices.append(c)

	parentid = forms.ChoiceField(choices=choices)
	class Meta:
		model=Category
		fields=['id','parentid','name','description']

class ProductForm(ModelForm):
	class Meta:
		model=Product
		fields='__all__'

class FeatureLookupForm(ModelForm):
	class Meta:
		model= FeatureLookup
		fields= '__all__'

class FeatureValueForm(ModelForm):
	class Meta:
		model: FeatureValue
		fields: '__all__'

class CartForm(ModelForm):
	class Meta:
		model: Cart
		fields: '__all__'

class OrderForm(ModelForm):
	class Meta:
		model: Order
		fields: '__all__'

class OrderItemForm(ModelForm):
	class Meta:
		model: OrderItem
		fields: '__all__'

class ShippingForm(ModelForm):
	class Meta:
		model: Shipping
		fields: '__all__'
