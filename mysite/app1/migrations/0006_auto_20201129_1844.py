# Generated by Django 3.1.2 on 2020-11-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20201129_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(default='write description'),
        ),
    ]
