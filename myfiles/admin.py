from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminServise(admin.ModelAdmin):
    list_display = ["id", 'name', 'text', 'image', 'data']

admin.site.register(Servise, AdminServise)

class AdminProjects(admin.ModelAdmin):
    list_display = ['id', 'name', 'adres', 'image', 'data']

admin.site.register(Project, AdminProjects)

class AdminHome(admin.ModelAdmin):
    list_display = ["id", 'name', 'text', 'image', 'data']

admin.site.register(Home, AdminHome)

class AdminContact(admin.ModelAdmin):
    list_display = ["id", 'name', 'lastname', 'email', 'text', 'data']

admin.site.register(Contact, AdminContact)

class AdminAbout(admin.ModelAdmin):
    list_display = ["id", 'name', 'yonalish', 'text', 'image', 'data']

admin.site.register(About, AdminAbout)

class AdminYonalish(admin.ModelAdmin):
    list_display = ["id", 'nomi']

admin.site.register(Yonalish, AdminYonalish)
