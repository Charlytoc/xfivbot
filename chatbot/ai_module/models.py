from django.db import models
from ..authenticate.models import Organization, AgentEngine
# Create your models here.
from django.utils.text import slugify


class PromptTemplate(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, help_text='This added automatically using the name')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None, help_text='Explain what this prompt pretends to do')
    engine = models.ForeignKey(AgentEngine, on_delete=models.CASCADE, null=True, help_text='The AI agent used to complete this prompt')
    prompt = models.TextField(max_length=3499,help_text='This will be the body of the prompt, what the AI will receive to provide an answer')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        from .actions import track_template_versions
        self.slug = slugify(self.name)
        super().save(*args, **kwargs) 
        track_template_versions(self)

class PromptTemplateVersion(models.Model):
    number = models.IntegerField(default=1)
    template = models.ForeignKey(PromptTemplate, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

