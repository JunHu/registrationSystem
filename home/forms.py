#!/usr/bin/env python
# coding=utf-8
from django import forms
from home.models import ApplyInfo
class ApllyInfoForm(forms.ModelForm):
    class Meta:
        model=ApplyInfo
    
    widgets={
        'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':u"姓名"})
    }
