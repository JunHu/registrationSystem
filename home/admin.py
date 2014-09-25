from django.contrib import admin
from models import *

RegisterClass = (
    ApplyInfo,
)

for temp in RegisterClass:
    admin.site.register(temp)
