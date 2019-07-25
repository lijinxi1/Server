from django.urls import re_path
from .views import qrmanage,qrgenerate
urlpatterns=[
    re_path('^qrmanage/',qrmanage,name='二维码生成管理'),
    re_path('^qrgenerate/',qrgenerate,name='二维码')
]