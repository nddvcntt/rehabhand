# Generated by Django 4.0.3 on 2022-04-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='exercise',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='general',
            name='patient',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
