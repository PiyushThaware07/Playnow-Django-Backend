from django.contrib import admin
from . models import *

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name","created_by","updated_by","is_active"]

class MovieAdmin(admin.ModelAdmin):
    list_display = ["title","genre","created_by","updated_by","is_active"]

admin.site.register(Genre,GenreAdmin)
admin.site.register(Movie,MovieAdmin)