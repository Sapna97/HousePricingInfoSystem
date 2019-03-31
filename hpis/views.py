from django.shortcuts import render, reverse
from .forms import MyForm
from django.http import HttpResponseRedirect

def home(request): # the function will take request as input
    return render(request, 'index.html')

def parameters(request):
    submitbutton = request.POST.get("submit")
    context = {}
    if request.method == "POST":
        form = MyForm(request.POST)
        
        if form.is_valid():
            area_type =  form.cleaned_data.get("area_type")
            loc =   form.cleaned_data.get("location")
            bedrms =   form.cleaned_data.get("bedrooms")
            hallkitchen = form.cleaned_data.get("hallkitchen")
            areasqft =  form.cleaned_data.get("area_sqft")
            bathrms =  form.cleaned_data.get("bathrooms")
            balcns =  form.cleaned_data.get("balconies")
            context = {'form':form, 'area_type':area_type, 'loc':loc, 'bedrms':bedrms, 'hallkitchen':hallkitchen,'areasqft':areasqft, 'bathrms':bathrms, 'balcns':balcns, 'submitbutton':submitbutton}
            print(context)
            return render(request, 'index.html', context)
        else:
            return HttpResponseRedirect(reverse('home'))
    else:
        form = MyForm()
        context = {'form':form}
        return render(request, 'index.html', context)


 # def parameters(request):
 #    context = {}
 #    if request.method == "POST":
 #        form = ParameterForm(request.POST)
 #        context['form'] = form
 #        if form.is_valid():
 #        	f = form.save()
 #        	return HttpResponseRedirect(reverse('home'))
 #        else:
 #        	return render(request, 'index.html', context)
 #    else:
 #        form = ParameterForm()
 #        context['form'] = form
 #        return render(request, 'index.html', context)        
 #       