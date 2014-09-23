from django.db import models

# Create your models here.


class ApplyInfo(models.Model):
    student_name=models.CharField(max_length=20,blank=False,verbose_name=u"姓名")
    sex=models.CharField(blank=False,verbose_name=u"性别")
    student_id=models.CharField(primary_key=True,max_length=9,min_length=9,blank=False,verbose_name=u"学号")
    tel_num=models.CharField(blank=False,verbose_name=u"电话")
    email=models.EmailField(blank=False,verbose_name=u"邮箱")
    apartment=models.IntegerField(blank=False,verbose_name=u"学部")
    college=models.IntegerField(blank=False,verbose_name=u"院系")
    wish_first=models.IntegerField(blank=False,verbose_name=u"第一志愿")
    wish_second=models.IntegerField(blank=False,verbose_name=u"第二志愿")
    self_introduction=models.TextField(max_length=600,blank=True,null=True,verbose_name=u"自我介绍")

