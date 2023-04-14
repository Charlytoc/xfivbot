

def track_template_versions(template):
    from .models import PromptTemplateVersion
    last_version = PromptTemplateVersion.objects.filter(template__id = template.id).order_by('-created_at').first()
    number = 1 if last_version is None else last_version.number + 1
    new_version = PromptTemplateVersion.objects.create(template=template, number=number, body=template.body)
    new_version.save()


def execute_a_template(template):
    print(template.prompt)