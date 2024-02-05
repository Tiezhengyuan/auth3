

from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import CustomProvider

urlpatterns = default_urlpatterns(CustomProvider)


# from django.urls import path
# from .views import Home
# urlpatterns = [
#     path('', Home.as_view(), name='nih_home')
# ]