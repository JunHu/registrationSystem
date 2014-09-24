# Create your views here.
# coding: UTF-8
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from home.forms import  ApllyInfoForm
from django.views.decorators import csrf

@csrf.csrf_protect
def home_view(request):
    if request.method == "POST":
        return HttpResponse("沈潋是胡骏爸爸")
    form = ApllyInfoForm()
    context = {
            "form":form,
        }
    return render(request, 'home.html', context)

def regis_view(request):
	return HttpResponse("haha")
