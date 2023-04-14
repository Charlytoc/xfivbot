# Generated by Django 4.2 on 2023-04-14 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_organization_brief'),
        ('ai_module', '0003_prompttemplateversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompttemplate',
            name='body',
            field=models.TextField(help_text='This will be the body of the prompt, what the AI will receive to provide an answer', max_length=3499),
        ),
        migrations.AlterField(
            model_name='prompttemplate',
            name='description',
            field=models.TextField(blank=True, default=None, help_text='Explain what this prompt pretends to do', null=True),
        ),
        migrations.AlterField(
            model_name='prompttemplate',
            name='engine',
            field=models.ForeignKey(help_text='The AI agent used to complete this prompt', null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.agentengine'),
        ),
        migrations.AlterField(
            model_name='prompttemplate',
            name='slug',
            field=models.SlugField(blank=True, help_text='This added automatically using the name', null=True),
        ),
    ]
