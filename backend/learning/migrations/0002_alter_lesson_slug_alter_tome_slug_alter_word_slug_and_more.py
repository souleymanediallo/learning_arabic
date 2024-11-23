# Generated by Django 5.1.3 on 2024-11-23 22:03

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tome',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='QuizHistory',
            fields=[
                ('is_correct', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_histories', to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_histories', to='learning.word')),
            ],
        ),
        migrations.CreateModel(
            name='QuizScore',
            fields=[
                ('total_attempts', models.PositiveIntegerField(default=0)),
                ('total_correct', models.PositiveIntegerField(default=0)),
                ('total_incorrect', models.PositiveIntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_score', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]