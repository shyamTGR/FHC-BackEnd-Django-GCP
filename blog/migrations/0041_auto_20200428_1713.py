# Generated by Django 2.0 on 2020-04-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20200428_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='language',
            field=models.CharField(choices=[('TL', 'Telugu'), ('EN', 'English'), ('HN', 'Hindi')], default='TL', max_length=2),
        ),
    ]
