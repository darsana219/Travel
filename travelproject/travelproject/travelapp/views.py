from django.http import HttpResponse
from .models import Place
from .models import People
from django.shortcuts import render

# Create your views here.
def demo(requset):
    obj = Place.objects.all()
    obj1 = People.objects.all()
    return render(requset,'index.html',{'result':obj,'result1':obj1})
# def calculation(request):
#     a = int(request.GET['num1'])
#     b = int(request.GET['num2'])
#     res1 = a + b
#     res2 = a - b
#     res3 = a * b
#     res4 = a // b
#     return render(request,"result.html",{'res':res1,'resu':res2,'resul':res3,'result':res4})