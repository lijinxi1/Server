from django.urls  import re_path
from .views import *
urlpatterns=[
    re_path('^upload/$',upload,name='上传'),
    re_path('^upload_register/$',upload_register,name='上传注册'),
    re_path('^upload_sign/$',upload_sign,name='上传签到'),
    re_path('^upload_sign/*',upload_sign,name='上传签到'),
]