# Generated by Django 4.2 on 2023-04-14 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_organization_brief'),
        ('ai_module', '0005_rename_body_prompttemplate_prompt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PromptTemplate',
            new_name='Template',
        ),
        migrations.RenameModel(
            old_name='PromptTemplateVersion',
            new_name='TemplateVersion',
        ),
    ]
