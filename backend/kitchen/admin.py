from django.contrib import admin

from .models import *

admin.site.register(Ingredient)
admin.site.register(Recepie)
admin.site.register(Quantity)