# Generated by Django 2.2.7 on 2019-11-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(null=True, verbose_name='date modified'),
        ),
    ]