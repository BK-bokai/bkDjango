# Generated by Django 2.2.7 on 2019-11-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
