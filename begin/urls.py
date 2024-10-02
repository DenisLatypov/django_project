from django.urls import path
from begin.views import index, help, defend


urlpatterns=[
    path('', index),
    path('help/', help),
    path('defend/', defend),
]