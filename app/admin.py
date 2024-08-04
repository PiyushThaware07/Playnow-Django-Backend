from django.contrib import admin
from . models import *

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title","created_by","created_at","is_active"]

admin.site.register(Movie,MovieAdmin)