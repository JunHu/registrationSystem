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
            'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':u"姓名"}),
            'sex':forms.ChoiceField(choices=SEX_CHOICES,required=True,widget=forms.Select(attrs={'class':'form-control',})),
            'student_id':forms.TextInput(attrs={"class":'form-control'}),
            'tel_num':forms.TextInput(attrs={"class":'form-control'}),
            'email':form.TextInput(atrrs={"class":'form-control'}),
            'apartment':forms.ChoiceField(choices=APARTMENT,required=True,widget=forms.Select(attrs={'class':'form-control'})),
            'college':forms.ChoiceField(choices=COLLEGE_DICT.get(0, None),widget=forms.Select(attrs={'class':'form-control'})),
            'wish_first':forms.ChoiceField(choices=CLASS_CHOICES,wiget=forms.Select(attrs={'class':'form-control'})),
            'wish_second':forms.ChoiceField(choices=CLASS_CHOICES,wiget=forms.Select(attrs={'class':'form-control'})),
            'self_introduction':forms.Textarea(attrs={'class':'form-control','placeholder':u"请做简单自我介绍，包括自己特长和参加科技竞赛获奖经历。"})
    }
