from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
		pass


class confirmEmail(View):
	def get(self, request):
		pass
	def post(self, request):
		pass




