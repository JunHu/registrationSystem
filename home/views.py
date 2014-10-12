# Create your views here.
# coding: UTF-8
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from home.forms import  ApllyInfoForm, ClassForm, EntryInfoForm
from django.views.decorators import csrf
from django.core.urlresolvers import reverse

from const import *

@csrf.csrf_protect
def home_view(request):
    if request.method == "POST":
        form = ApllyInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home.views.response_view"))
    else:        
        form = ApllyInfoForm()
    context = {
            "form":form,
        }
    return render(request, 'home.html', context)

def entry_view(request):
    print "---" * 100
    if request.method == "POST":
        form = EntryInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home.views.response2_view"))
    else:        
        form = EntryInfoForm()
    context = {
            "form":form,
        }
    return render(request, 'entry.html', context)


def response_view(request):
	return render(request, "response.html", {})

def response2_view(request):
    return render(request, "response2.html", {})

def export_view(request):
    form = ClassForm()
    context = {
        "form": form,
    }
    return render(request, "export.html", context)
