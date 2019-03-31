from django import forms


class MyForm(forms.Form):
	area_type =  forms.CharField(max_length=200)
	location =   forms.CharField(max_length=200)
	bedrooms =   forms.IntegerField()
	hallkitchen = forms.IntegerField()
	area_sqft =  forms.IntegerField()
	bathrooms =  forms.IntegerField()
	balconies =  forms.IntegerField()

	 
