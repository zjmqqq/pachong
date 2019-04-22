from django.http import HttpResponse
from pachong.models import movie


# 数据库操作
def testdb(request):
    response1=''
    response=''
    list = movie.objects.all()
    for var in list:
        response1 += (var.name + "<br>")
    response = response1
    return HttpResponse("<p>" + response + "</p>")