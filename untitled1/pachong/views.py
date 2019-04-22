from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from pachong.models import movie
from pachong.models import computerinfo

from django.core.paginator import Paginator

def index(request):
    return render(request, 'pachong/index.html',{'hello':'Hello,Pachong1!'})

def lalala(request):
    list=movie.objects.all()
    name=list[0].name
    return  render(request,'pachong/lalala.html',{'movie':name})

def computer1(request,num):
    li=computerinfo.objects.all()[:100]
    pgs=Paginator(li,10)
    if(num>pgs.num_pages):
        return render(request, 'pachong/computer.html', {"ls": pgs.page(pgs.num_pages)})
    if (num<=1):
        return render(request, 'pachong/computer.html', {"ls": pgs.page(1)})
    return render(request, 'pachong/computer.html',{"ls":pgs.page(num)})











