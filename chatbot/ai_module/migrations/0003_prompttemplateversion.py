# Generated by Django 4.2 on 2023-04-14 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ai_module', '0002_rename_decisiontemplate_prompttemplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromptTemplateVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai_module.prompttemplate')),
            ],
        ),
    ]
