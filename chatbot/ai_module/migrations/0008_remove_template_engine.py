# Generated by Django 4.2 on 2023-04-14 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai_module', '0007_template_ai_example_template_human_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='engine',
        ),
    ]