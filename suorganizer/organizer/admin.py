from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Tag)
admin.site.register(models.NewsLink)
admin.site.register(models.StartUp)
