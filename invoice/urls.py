from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
	path('', views.InvoiceListView.as_view(), name = 'index'),
]