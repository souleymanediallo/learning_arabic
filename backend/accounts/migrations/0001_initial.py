# Generated by Django 5.1.3 on 2024-11-23 16:44

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user_type', models.CharField(choices=[('HOMME', 'HOMME'), ('FEMME', 'FEMME')], default='HOMME', max_length=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('image', models.ImageField(blank=True, default='images/user.png', null=True, upload_to='images/%Y/')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
