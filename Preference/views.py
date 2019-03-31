from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from Preference.forms import ParameterForm

def home(request): # the function will take request as input
    return render(request, 'index.html')


def parameters(request):
    context = {}
    if request.method == "POST":
        form = ParameterForm(request.POST)
        context['form'] = form
        if form.is_valid():
        	f = form.save()
        	return HttpResponseRedirect(reverse('home'))
        else:
        	return render(request, 'index.html', context)
    else:
        form = ParameterForm()
        context['form'] = form
        return render(request, 'index.html', context)        


# def employee_add(request):
#     context = {}
#     if request.method == 'POST':
#         user_form = Userform(request.POST)
#         context['user_form'] = user_form
#         if user_form.is_valid():
#             u = user_form.save()
#             return HttpResponseRedirect(reverse('employee_list'))
#         else:
#             return render(request, 'employee/add.html', context)
#     else:
#     	user_form = Userform()
#     	context['user_form'] = user_form
#     	return render(request, 'employee/add.html', context)