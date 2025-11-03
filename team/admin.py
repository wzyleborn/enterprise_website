from django.contrib import admin

from team.models import Team


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name','title')
    search_fields = ('name',)


admin.site.register(Team, TeamAdmin)