# Generated by Django 2.1.4 on 2019-01-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siscontrol', '0015_comunicadoescolar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Di', 'Dibujo'), ('Ta', 'Taekwondo'), ('Ha', 'Hawaiano'), ('Da', 'Danza'), ('Ma', 'Marimba'), ('Vc', 'Vocalizacionycanto'), ('Bg', 'Bandadeguerra'), ('To', 'Tochito'), ('Es', 'Escolta'), ('Ba', 'Basquetbol'), ('Fu', 'Futbol'), ('Vo', 'Voleibol')], max_length=2, null=True),
        ),
    ]
