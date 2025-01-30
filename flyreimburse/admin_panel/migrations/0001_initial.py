# Generated by Django 5.1.5 on 2025-01-29 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(default='Unknown Agency', max_length=255)),
                ('contact_email', models.EmailField(default='default@email.com', max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_panel_agency', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='admin_panel.agency')),
                ('claim_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.claimsubmission')),
            ],
        ),
    ]
