# Generated by Django 2.2.7 on 2019-12-09 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['publish_date'], 'permissions': (('can_comment', 'Can comment'),)},
        ),
    ]
