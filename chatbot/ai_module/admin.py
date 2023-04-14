from django.contrib import admin
from .models import PromptTemplate, PromptTemplateVersion
# Register your models here.

@admin.register(PromptTemplate)
class PromptTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
