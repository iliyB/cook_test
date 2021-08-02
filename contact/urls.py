from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact_url'),
    path('feedback/', views.CreateContact.as_view(), name='feedback_url'),
]