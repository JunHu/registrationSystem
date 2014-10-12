from django.contrib import admin
from models import *

RegisterClass = (
    ApplyInfo,
    EntryInfo,
)

for temp in RegisterClass:
    admin.site.register(temp)
