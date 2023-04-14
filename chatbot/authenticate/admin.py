from django.contrib import admin
# Import the model
from .models import Organization, Agent, AgentCredentials

# Register the model
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ['name']

@admin.register(AgentCredentials)
class AgentCredentialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'organization', 'expires_at', 'agent')
    search_fields = ['created_by__first_name', 'created_by__last_name', 'created_by__email', 'organization']
    raw_id_fields = ['organization']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'documentation_url', 'name')
    search_fields = ['name']
