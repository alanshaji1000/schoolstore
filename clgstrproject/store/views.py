from django.shortcuts import render, get_object_or_404, redirect
from .models import Department,Course
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from .forms import FormSubmissionForm
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    departments = Department.objects.all()
    # Pass the departments to the template context
    context = {'departments': departments}
    return render(request, "home.html", context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('store:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('store:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                print("user created")
                return redirect(reverse('store:login'))
        else:
            messages.info(request, "Password not matching")
            return redirect('store:register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('store:store')
            #return render('/')
        else:
            #messages.info(request,"Invalid Credentials")
            return redirect('store:login')
    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def store(request):
    # Implement login logic here
    return render(request, 'store.html')


def form(request):
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            form.save()

            # messages.info(request, "Form submitted")
            return redirect('store:message')
            # return render(request, 'form.html')
    else:
        form = FormSubmissionForm()

    return render(request, 'form.html', {'form': form})


def message(request):
    return render(request, 'message.html')

