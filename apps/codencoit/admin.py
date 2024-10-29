from django.contrib import admin
from .models import *

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name','designation','address']
    ordering = ['name']


@admin.register(Industry)    
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id','name']

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display= ['id','title','client_name']
    ordering = ['id', 'title']
