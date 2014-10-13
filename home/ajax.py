from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.db.models import Q
from const import *
from models import *
from utility import info_xls_baseinformation
@dajaxice_register
def getCollege(request,apartment):
    apartment=int(apartment)
    college=COLLEGE_DICT.get(apartment,None)
    return simplejson.dumps({"college":college})

@dajaxice_register
def exportData(request, choose):
    message = ""
    choose = int(choose)
    obj = ApplyInfo.objects.filter(Q(wish_first = choose) | Q(wish_second = choose))
    class_type = CLASS_CHOICES[choose][1] 
    path = info_xls_baseinformation(request,obj,class_type)
    return simplejson.dumps({"message": message,"path":path})
