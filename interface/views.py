from django.shortcuts import render
from .models import Student
import os


# Create your views here.
def index(request):
    pics = []
    for img in os.listdir('./interface/static'):
        if img.endswith('png'):
            pics.append('/static/' + img)
    context = {}
    context['main'] = pics
    return render(request, 'interface/qrcode.html', context=context)





def train(request):
    q = request.GET.get('q')
    start_train = request.GET.get('train')
    post_list = Student.objects.filter(stu_class=q)
    context = {}
    context['caption'] = '人脸识别模型生成系统'
    context['post_list'] = post_list
    if q:
        dirs = str(q)+'/'
        file_path = settings.MEDIA_ROOT+dirs
        filename = os.listdir(file_path)
    if start_train == start_train:
        text = ''
        for p in post_list:
            if filename.count(p.stu_id) == 0:
                text = text+str(p.stu_id)+' '
                context['lack_stu'] = text
            else:
                st = FaceProcess(q, p.stu_id, False)
                print(os.path.curdir)
                st.train()

    return render(request, 'interface/train.html', context)


if __name__ == '__main__':
    print(os.curdir)
