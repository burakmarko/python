# Generated by Django 2.1.5 on 2019-11-11 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_delete_return'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='name_title',
            new_name='article_title',
        ),
    ]
