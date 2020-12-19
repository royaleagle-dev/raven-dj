from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
	path('', views.LoginView.as_view(), name = 'authIndex'),
	path('register', views.SignupView.as_view(), name = 'register'),
]