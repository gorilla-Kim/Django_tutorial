# Generated by Django 2.1.5 on 2019-02-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(default=123, max_length=15),
            preserve_default=False,
        ),
    ]