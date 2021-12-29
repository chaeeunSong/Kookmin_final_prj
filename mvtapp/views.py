from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from mvtapp.models import LectureDetail
from django.urls import reverse

def detail(request):
    #return HttpResponse('response detail')
    #return render(request, 'mvtapp/reg_meeting.html')

    if request.method == 'POST':
        title = request.POST.get('title')
        person = request.POST.get('person')
        meeting = request.POST.get('meeting')

        # ORM을 위한, 모델 오브젝트 생성
        data = LectureDetail()
        data.title = title
        data.person = person
        data.meeting = meeting

        data.save()

        #after input, for review datas in DB
        #datas = LectureDetail.objects.all()

        #return render(request, 'mvtapp/admin_board.html', context={'datas':datas})
        return HttpResponseRedirect(reverse('mvtapp:detail'))
    else:
        #pass
        datas = LectureDetail.objects.all()

    return render(request, 'mvtapp/admin_board.html', context={'datas':datas})


