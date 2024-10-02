from django.urls import path
from third.views import tv,cat,dog


urlpatterns=[
    path('tv/', tv),
    path('cat/', cat),
    path('dog/', dog),
]