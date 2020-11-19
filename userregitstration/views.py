from django.shortcuts import render, redirect, get_object_or_404
from .forms import Creatuserform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    form = Creatuserform(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account is created for {username}')
        Customer.objects.create(user=user)
        return redirect('/login')
    context = {'form': form}
    return render(request, "register.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')

    return render(request, "login.html", )
@login_required(login_url='login')
def home_view(request, *args, **kwargs):
    # queryset2 = request.user.customer
    # print('object_list2:', queryset2)

    # context = {

    # "object_list2": queryset2,
    # }

    return render(request, "home.html")