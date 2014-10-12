#coding: UTF-8

from django.db import models
from const import *
# Create your models here.


class ApplyInfo(models.Model):
    student_name=models.CharField(max_length=20,blank=False,verbose_name=u"姓名")
    sex=models.CharField(max_length=20,blank=False,choices=SEX_CHOICES,verbose_name=u"性别")
    student_id=models.CharField(primary_key=True,max_length=9,blank=False,verbose_name=u"学号")
    tel_num=models.CharField(max_length=20,blank=False,verbose_name=u"电话")
    email=models.EmailField(blank=False,verbose_name=u"邮箱")
    apartment=models.IntegerField(blank=False,choices=APARTMENT_CHOICES,verbose_name=u"学部")
    college=models.IntegerField(blank=False,choices=COLLEGE_CHOICES,verbose_name=u"院系")
    wish_first=models.IntegerField(blank=False,choices=CLASS_CHOICES,verbose_name=u"第一志愿")
    wish_second=models.IntegerField(blank=False,choices=CLASS_CHOICES,verbose_name=u"第二志愿")
    self_introduction=models.TextField(max_length=600,blank=True,null=True,verbose_name=u"自我介绍")
    class Meta:
        verbose_name = "在线报名表"
        verbose_name_plural = "在线报名表"
    def __unicode__(self):
        return self.student_name

class EntryInfo(models.Model):
    student_name=models.CharField(max_length=20,blank=False,verbose_name=u"姓名")
    sex=models.CharField(max_length=20,blank=False,choices=SEX_CHOICES,verbose_name=u"性别")
    student_id=models.CharField(max_length=9,blank=False,verbose_name=u"学号")
    tel_num=models.CharField(max_length=20,blank=False,verbose_name=u"电话")
    email=models.EmailField(blank=False,verbose_name=u"邮箱")
    apartment=models.IntegerField(blank=False,choices=APARTMENT_CHOICES,verbose_name=u"学部")
    college=models.IntegerField(blank=False,choices=COLLEGE_CHOICES,verbose_name=u"院系")
    wish_type=models.IntegerField(blank=False,choices=CLASS_CHOICES,verbose_name=u"志愿")
    wish_grade=models.IntegerField(blank=False,choices=YES_NO,verbose_name=u"是否为第一志愿")
    self_introduction=models.TextField(max_length=600,blank=True,null=True,verbose_name=u"自我介绍")
    class Meta:
        unique_together = (("student_id", "wish_grade", ), ("student_id", "wish_type", ), )
        verbose_name = "录入报名表"
        verbose_name_plural = "录入报名表"
    def __unicode__(self):
        return self.student_name
