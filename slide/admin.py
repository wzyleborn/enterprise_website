from django.contrib import admin
from slide.models import Slide

class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Slide, SlideAdmin)

# Register your models here.
