# Generated by Django 2.1.5 on 2019-11-11 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20191111_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='credit_title',
            new_name='article_title',
        ),
    ]
