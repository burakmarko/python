# Generated by Django 2.1.5 on 2019-11-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20191028_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="ім'я")),
                ('funds', models.TextField(verbose_name='кількість коштів')),
                ('pub_date', models.DateTimeField(verbose_name='дата')),
            ],
        ),
    ]
