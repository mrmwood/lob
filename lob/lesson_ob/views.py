from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from lesson_ob.forms import RegistrationForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the lesson ob index.")

def test(request):
    return render(request,"lesson_ob/index.html")

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
