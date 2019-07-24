from django.urls import re_path

from .views import register,register_result


urlpatterns=[
    re_path('^register/$',register,name='注册'),
    re_path('^register_result',register_result,name='注册提交')
]