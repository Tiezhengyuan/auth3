'''
'''

from django.urls import path
from django.views.generic.base import TemplateView, RedirectView

from .views import OwnerView, SessionView, IndexView, TaskView

urlpatterns = [
    path('owners/', OwnerView.as_view(), name='owners'),
    path('sessions/', SessionView.as_view(), name='sessions'),
    path('', IndexView, name='index'),
    # path('', TemplateView.as_view(template_name='reporting/index.html'), name='index'),
    path('task/', TaskView, name='task'),
]