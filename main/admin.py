from django.contrib import admin
from main import models
# Register your models here.
admin.site.register(models.News)
admin.site.register(models.Blog)
admin.site.register(models.Comments)
