from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from broker.forms import SignUpForm, EditProfileForm, Advform
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from broker.models import Adv


# from broker.forms import EditProfileForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('my_profile')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})



def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next',None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('my_profile'))
        else:
            context["error"] = "Provide Valid Credentials!!"    
            return render(request, "auth/login.html", context)    
    else:
        return render(request, "auth/login.html", context)


@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'auth/profile.html', args)



# function to edit user details entered during register
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('my_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'auth/profile_edit.html', args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('my_profile'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'auth/change_password.html', args)


#to edit further details
class ProfileUpdate(UpdateView):
    fields = [ 'description', 'website', 'phone', 'image']
    template_name = 'auth/profile_update.html'
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        return self.request.user.profile


#form to add advertisement
# def create_ad(request):
#     context = {}
#     if request.method == 'POST':
#         advform = Advform(request.POST)
#         context['advform'] = advform
#         if advform.is_valid():
#             a = advform.save()
#             return HttpResponseRedirect(reverse('my_profile'))
#         else:
#             return render(request, 'adv/add.html', context)
#     else:
#     	advform = Advform()
#     	context['advform'] = advform
#     	return render(request, 'adv/add.html', context)



def create_ad(request):
    if request.method == "POST":
        advform = Advform(request.POST)
        if advform.is_valid():
            adv = advform.save(commit=False)
            adv.broker = request.user.profile
            adv.save()
            return redirect('my_profile')
    else:
        advform = Advform()
        return render(request, 'adv/add.html', {'advform': advform})

 
class AdvListView(ListView):
    template_name = 'adv/adv_list.html'

    def get_queryset(self):
        advs = Adv.objects.filter(broker_id=self.request.user.id)
        return advs
        


#alternative for filtering
# advs = Adv.objects.get(broker_id=user.profile.id)