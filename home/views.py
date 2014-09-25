# Create your views here.
# coding: UTF-8
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from home.forms import  ApllyInfoForm
from django.views.decorators import csrf
from django.core.urlresolvers import reverse

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

def response_view(request):
	return render(request, "response.html", {})
