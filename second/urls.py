from django.urls import path
from second.views import box,car,wheel


urlpatterns=[
    path('box/', box),
    path('car/', car),
    path('wheel/', wheel),
]