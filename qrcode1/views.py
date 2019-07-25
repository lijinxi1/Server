from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from interface.models import Course
# Create your views here.
from qrcode1.static.img.qrcode_generate import qrcode_genearte

def qrmanage(request):
    if request.method=='GET':
        return render(request,'qrcode1/qrmanage.html')
    else:
        course = request.POST.get('course')
        post_list = Course.objects.filter(course=course)
        context = {}
        context['caption'] = '签到二维码生成系统'
        context['post_list'] = post_list
        context['course']=course
        return render(request, 'qrcode1/qrmanage.html', context=context)

def qrgenerate(request):
    course=request.POST.get('course')
    qrcode_genearte(course)
    img='../../static/img/'+course+'.png'
    context={}
    context['course']=course
    context['img']=img

    return render(request,'qrcode1/qrcode.html',context=context)

