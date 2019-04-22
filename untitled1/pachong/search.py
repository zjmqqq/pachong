from django.http import HttpResponse
from django.shortcuts import render_to_response
from pachong.models import uesrs
def search_form(request):
    #return render_to_response('pachong/search_form.html')
    return render_to_response('pachong/register.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    user=uesrs()
    if request.method == 'GET':
        user.username=request.GET['username']
        user.userpassword=request.GET['password']
        user.usersex=request.GET['gender']
        user.save()
        message = 'success register'
    else:
        message = 'failed register'
    return HttpResponse(message)


