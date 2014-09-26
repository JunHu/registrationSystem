#!/usr/bin/env python
# coding=utf-8
from django import forms
from home.models import ApplyInfo
from const import *

class ClassForm(forms.Form):
    classes = forms.ChoiceField(choices = CLASS_CHOICES, required = True, label = "实践班", widget = forms.Select(attrs={"class": "form-control regis-input"}))

class ApllyInfoForm(forms.ModelForm):
    def clean_wish_second(self):
        first = self.cleaned_data.get("wish_first")
        second = self.cleaned_data.get("wish_second")
        if first == second:
            raise forms.ValidationError("两个志愿不能相同")
        return second
    class Meta:
        model=ApplyInfo
    
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control regis-input','placeholder':u"姓名"}),
            'sex':forms.Select(attrs={'class':'form-control regis-input', 'placeholder':u'性别'}),
            'student_id':forms.TextInput(attrs={"class":'form-control regis-input', 'placeholder': '学号'}),
            'tel_num':forms.TextInput(attrs={"class":'form-control regis-input', 'placeholder': '电话'}),
            'email':forms.TextInput(attrs={"class":'form-control regis-input', 'placeholder': '邮箱'}),
            'apartment':forms.Select(attrs={'class':'form-control regis-input', }),
            'college':forms.Select(attrs={'class':'form-control regis-input'}),
			'wish_first':forms.Select(attrs={'class':'form-control regis-input'}),
            'wish_second':forms.Select(attrs={'class':'form-control regis-input'}),
            'self_introduction':forms.Textarea(attrs={'class':'form-control','placeholder':u"请做简单自我介绍，包括自己特长和参加科技竞赛获奖经历(300字以内)。"})
    }
