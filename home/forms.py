#!/usr/bin/env python
# coding=utf-8
from django import forms
from home.models import ApplyInfo
from const import *
class ApllyInfoForm(forms.ModelForm):
    def clean(self):
        clean=self.cleaned_data
        first = self.cleaned_data["wish_first"]
        second = self.cleaned_data["wish_second"]
        if first == second:
            raise forms.ValidationError("两个志愿不能相同")
        return clean
    class Meta:
        model=ApplyInfo
    
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control regis-input','placeholder':u"姓名"}),
            'sex':forms.Select(attrs={'class':'form-control regis-input',}),
            'student_id':forms.TextInput(attrs={"class":'form-control regis-input'}),
            'tel_num':forms.TextInput(attrs={"class":'form-control regis-input'}),
            'email':forms.TextInput(attrs={"class":'form-control regis-input'}),
            'apartment':forms.Select(attrs={'class':'form-control regis-input'}),
            'college':forms.Select(attrs={'class':'form-control regis-input'}),
			'wish_first':forms.Select(attrs={'class':'form-control regis-input'}),
            'wish_second':forms.Select(attrs={'class':'form-control regis-input'}),
            'self_introduction':forms.Textarea(attrs={'class':'form-control','placeholder':u"请做简单自我介绍，包括自己特长和参加科技竞赛获奖经历(300字以内)。"})
    }
