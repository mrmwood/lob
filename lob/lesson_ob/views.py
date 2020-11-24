from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
#import here any classes I need from forms.py
from lesson_ob.forms import RegistrationForm, AccountAuthenticationForm
from django.http import HttpResponse
from lesson_ob.models import Account
# Create your views here.


def index(request):
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request,"lesson_ob/index.html", context)

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('index')
		else:
			context['registration_form'] = form
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'lesson_ob/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

def login_view(request):

    context = {}

    user = request.user
    #if the user is already logged in then we want to redirect them to the home screen
    if user.is_authenticated:
        return redirect("index")

    #If you are tryign to login
    if request.POST:
        #Get the data from the  AccountAuthenticationForm form in forms.py
        form = AccountAuthenticationForm(request.POST)
        #check if the data is valid i.e. everything that is there is entered and correct
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            #authenticate if there is a user obecject with these credentials
            user = authenticate(email=email, password=password)

            #if there is a user with these credentials log them in and redirect to home sreen
            if user:
                login(request, user)
                return redirect("index")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'lesson_ob/login.html', context)
