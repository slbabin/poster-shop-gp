# Generated by Django 3.2.23 on 2024-01-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='poster',
            name='sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
