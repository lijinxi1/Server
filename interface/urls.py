# -*- coding : utf-8 -*-
# @author : Dell
# @time : 16:53   2019/7/14
# @filename : urls.py
from django.urls import path
from .views import index, pictures_save, train
urlpatterns=[
    path('train/', train, name='人脸模型训练'),
    path('pictures_save/', pictures_save, name='图片上传'),
    path('qrcode/',index,name='二维码'),
]