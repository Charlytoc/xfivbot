from django.contrib import admin
from .models import Template, TemplateVersion
# Register your models here.

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
