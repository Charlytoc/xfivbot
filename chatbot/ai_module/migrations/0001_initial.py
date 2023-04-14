# Generated by Django 4.2 on 2023-04-14 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authenticate', '0002_agent_agentengine_agentcredentials'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('engine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.agentengine')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.organization')),
            ],
        ),
    ]
