from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
import uuid
from django.core.mail import send_mail
from users.models import Profile

# Create your views here.

class LoginView(View):

	def get(self, request):
		return render(request, 'users/authIndex.html')

	def post(self, request):
		username = request.POST.get('email')
		password = request.POST.get('password')

		#debug
		print(username)
		print(password)
		#---------------

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, "User successfully Logged in")
			return redirect ("invoice:index")
		else:
			messages.warning(request, "User not logged in. Pls check credentials")
			return redirect ("users:authIndex")

class SignupView(View):
	def get(self, request):
		return render(request, "users/authSignup.html")

	def post(self, request):
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		othername = request.POST.get('othername')
		dob = request.POST.get('dob')
		password = request.POST.get('password')
		email = request.POST.get('email')

		user = User(
				username = email,
				email = email,
				password = password

			)
		
		user.first_name = firstname
		user.last_name = lastname
		user.save()

		messages.success(request, "Registration Successful")
		return redirect('users:confirm', username = email)


class ConfirmRegister(View):

	def get(self, request, username):

		user = User.objects.get(username=username)
		email = user.email
		user = Profile.objects.get(user=user)
		verification_code = user.verification_code
		
		send_mail(
    		'Account Verification Code',
    		verification_code,
    		'from@example.com',
    		['to@example.com'],
    		fail_silently=False,
		)

		context = {
		'email':email,
		}



		return render(request, "users/confirm.html", context)

	def post(self, request, username):
		verify = request.POST.get('verify')
		user = User.objects.get(username=username)
		user = Profile.objects.get(user = user)
		
		#debug
		print (user.verification_code)

		if verify == user.verification_code:
			messages.success(request, "Verification successful")
			return redirect ("users:profile")
		else:
			messages.warning(request, "Verification not successful, Pls try again")
			return redirect("users:confirm", username=username)