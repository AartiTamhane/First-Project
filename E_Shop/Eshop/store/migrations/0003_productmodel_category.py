# Generated by Django 3.2.4 on 2021-06-24 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_categorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.categorymodel'),
        ),
    ]
