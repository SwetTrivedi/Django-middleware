from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    print("i am view")
    return HttpResponse("This is Home Page")

def excp(request):
    print("i am excep")
    a=10/0
    return HttpResponse("This is Before view ")


def user_info(request):
    print("This is user info")
    context={"name":"rahul"}
    return TemplateResponse(request,"user.html",context)