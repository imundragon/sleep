# Generated by Django 5.0.6 on 2024-07-04 12:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст коментария')),
                ('create_date_comment', models.DateField(auto_now=True, verbose_name='Дата')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.blog', verbose_name='Блог')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
