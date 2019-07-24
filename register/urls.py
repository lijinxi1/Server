from django.urls import re_path

from .views import register


urlpatterns=[
    re_path('^register',register,name='注册')
]