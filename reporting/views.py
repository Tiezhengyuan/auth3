from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.http import HttpResponse

from .models import Owner, Session



class OwnerView(LoginRequiredMixin, ListView):
    template_name = 'reporting/owner.html'
    queryset = Owner.objects.all()
    context_object_name = 'owner'


class SessionView(LoginRequiredMixin, ListView):
    template_name = 'reporting/session.html'
    queryset = Session.objects.all()
    context_object_name = 'session'



def IndexView(request):
    return render(None, 'reporting/index.html')
