# Generated by Django 2.1.3 on 2018-11-16 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
