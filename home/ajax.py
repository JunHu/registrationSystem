from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from const import *

@dajaxice_register
def getCollege(request,apartment):
    apartment=int(apartment)
    college=COLLEGE_DICT.get(apartment,None)
    print college
    return simplejson.dumps({"college":college})


