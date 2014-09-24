# Create your views here.
# coding: UTF-8
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect 


def home_view(request):
    context = {}
    return render(request, 'home.html', context)


