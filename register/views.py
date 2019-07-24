from django.shortcuts import render
from django.core.exceptions import *
# Create your views here.
from .models import Teacher,Student
def register(requests):
    return render(requests,'register/register.html')


def register_result(requests):
    identity=requests.POST.get('identity')
    _id=requests.POST.get('_id')
    name=requests.POST.get('name')
    class_office=requests.POST.get('class_office')
    email=requests.POST.get('email')
    phone=requests.POST.get('phone')
    addr=requests.POST.get('address')
    print(identity)
    if identity=='teacher':
        if _id!='':
            try:
                t=Teacher.objects.get(teacher_id=_id)
            except  ObjectDoesNotExist:
                text="教师已成功注册"
                t = Teacher(teacher_id=_id, teacher_name=name, teacher_office=class_office,
                            teacher_email=email, teacher_phone=phone, teacher_addr=addr)
                t.save()
            else:
                t.teacher_id=_id
                t.teacher_email=email
                t.teacher_office=class_office
                t.teacher_name=name
                t.teacher_phone=phone
                t.teacher_addr=addr
                t.save()
                text="教师信息已更新"

    else:
        if _id!='':
            try:
                s=Student.objects.get(stu_id=_id)
            except ObjectDoesNotExist:
                s=Student(stu_id=_id,stu_name=name,stu_class=class_office,
                      stu_email=email,stu_phone=phone,stu_addr=addr)
                s.save()
                text="学生已成功注册"
            else:
                s.stu_id=_id
                s.stu_class=class_office
                s.stu_addr=addr
                s.stu_phone=phone
                s.stu_email=email
                s.stu_name=name
                s.save()
                text='学生信息已更新'

    context={}
    context['text']=text
    context['st_id']=_id
    context['name']=name
    context['class_office']=class_office
    context['email']=email
    context['phone']=phone
    context['addr']=addr
    context['identity']=identity
    return render(requests,'register/register_result.html',context=context)
