from django.contrib import admin

# Register your models here.
from .models import River, caughtFish

admin.site.register(River)
admin.site.register(caughtFish)