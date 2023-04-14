from django.db import models
from ..authenticate.models import Organization
# Create your models here.
from django.utils.text import slugify


class Template(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, help_text='This added automatically using the name')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None, help_text='Explain what this prompt pretends to do')
    prompt = models.TextField(max_length=3499,help_text='This will be the body of the prompt, what the AI will receive to provide an answer')
    human_example= models.CharField(max_length=500, null=True, blank=True)
    ai_example= models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        from .actions import track_template_versions
        self.slug = slugify(self.name)
        super().save(*args, **kwargs) 
        track_template_versions(self)

class TemplateVersion(models.Model):
    number = models.IntegerField(default=1)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

