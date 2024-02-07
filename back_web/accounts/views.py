from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import CustomUserCreationForm


class HomeView(TemplateView):
    template_name = 'home.html'
    # def get(self, request, *args, **kwargs):
    #     context = {'name': 'Home'}
    #     return render(request, 'home.html', context)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"