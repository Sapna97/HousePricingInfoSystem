from django import forms
from .models import Parameters


class ParameterForm(forms.ModelForm):

    class Meta:
        model = Parameters
        fields = ['area_type', 'location', 'bedrooms', 'hallkichen', 'area_sqft', 'bathrooms', 'balconies']
 




