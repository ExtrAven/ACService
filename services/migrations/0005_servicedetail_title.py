# Generated by Django 5.1.4 on 2024-12-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_servicedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]