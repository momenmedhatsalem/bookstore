from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy

from .froms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"