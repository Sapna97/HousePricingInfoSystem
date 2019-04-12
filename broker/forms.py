from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from broker.models import Adv

#edit registration details form
class EditProfileForm(UserChangeForm):
    template_name='auth/profile_edit.html'

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
        )


#registration form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



#Advertisement form
class Advform(forms.ModelForm):
	
	class Meta:
		model = Adv
		fields = ['title', 'bath', 'balcony', 'bedrooms', 'area_sqft', 'area_type', 'hk', 'location',]
