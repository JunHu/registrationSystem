from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.db.models import Q
from const import *
from models import *
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
    return simplejson.dumps({"message": message})
