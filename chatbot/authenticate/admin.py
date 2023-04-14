from django.contrib import admin
# Import the model
from .models import Organization

# Register the model
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ['name']
