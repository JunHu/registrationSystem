#!/usr/bin/env python
# coding=utf-8
'''
 File Name: home/urls.py
 Author: shenlian
 Created Time: 2014年09月23日 星期二 21时30分10秒
'''
from django.conf.urls import patterns, url,include
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from home import views as home_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(
        r'^regis',
        home_view.regis_view,
    ),    
)
