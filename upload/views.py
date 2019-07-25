from django.http import HttpResponseRedirect
from django.shortcuts import render
from register.models import Student
from django.shortcuts import redirect
from register.models import Teacher
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
import os
from ImageProcess.Process import FaceProcess
# Create your views here.


def upload(request):
    return render(request,'upload/upload.html')

def upload_register(request):
    data_folder = './DataSet/PICS'
    context = {}
    if request.method=="POST":
        stu_id=request.POST.get('stu_id')
        stu_class=request.POST.get('class')
        files = request.FILES.getlist("files[]")
        data_folder=os.path.join(data_folder,stu_class,stu_id)
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        i=0
        for f in files:
            with open(os.path.join(data_folder,f.name),'wb+') as dst:
                for chunk in f.chunks():
                    dst.write(chunk)
        # 从数据中查询姓名
        try:
            s=Student.objects.get(stu_id=stu_id)
        except ObjectDoesNotExist:
            text="-您还未注册 请先注册 "
            name=''
        else:
            text='图片传成功'
            name=s.stu_name
        context['name']=name
        context['stu_id'] = stu_id
        context['data_folder']=data_folder
        context['class'] = stu_class
        context['text']=text

        # 训练上传数据
        if name!='':
            try:
                fp=FaceProcess(stu_class,stu_id)
                fp.train()
            except Exception:
                trained="训练异常"
            else:
                trained='训练成功'
        else:
            trained=''
        context['trained']=trained
    return render(request,'upload/upload_register.html',context=context)


def upload_sign(request):
    data_folder = './DataSet/PICS'
    context = {}
    if request.method=="POST":
        stu_id=request.POST.get('stu_id')
        stu_class=request.POST.get('class')
        files = request.FILES.getlist("files[]")
        data_folder=os.path.join(data_folder,stu_class,stu_id)
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        i=0
        for f in files:
            with open(os.path.join(data_folder,f.name),'wb+') as dst:
                for chunk in f.chunks():
                    dst.write(chunk)
        # 从数据中查询姓名
        try:
            s=Student.objects.get(stu_id=stu_id)
        except ObjectDoesNotExist:
            text="-您还未注册 请先注册 "
            name=''
        else:
            text='图片传成功'
            name=s.stu_name
        context['name']=name
        context['stu_id'] = stu_id
        context['class'] = stu_class
        context['text']=text

        # 训练上传数据
        if name!='':
            try:
                fp=FaceProcess(stu_class,stu_id)
                recognized=fp.face_recognition()
            except Exception:
                recognized_result="识别异常"
            else:
                if recognized is not  None:
                    if recognized:
                        recognized_result='识别成功'
                    else:
                        recognized_result='识别失败 请重新上传照片识别'
                else:
                    recognized_result='未能检测到人脸 请重试'
        else:
            recognized_result='用户不存在 无法识别'
        context['recognized_result']=recognized_result
    return render(request,'upload/upload_sign.html',context=context)


