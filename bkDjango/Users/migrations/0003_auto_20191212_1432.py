# Generated by Django 2.2.7 on 2019-12-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20191212_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fullName',
            field=models.CharField(max_length=128, verbose_name='全名'),
        ),
    ]
