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
        form = ApllyInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("successfully!")
    else:        
        form = ApllyInfoForm()
    print form.errors
    context = {
            "form":form,
        }
    return render(request, 'home.html', context)

def regis_view(request):
	return HttpResponse("haha")
