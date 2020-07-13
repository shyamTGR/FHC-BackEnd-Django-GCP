# Generated by Django 2.0 on 2020-04-17 08:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='slug', editable=True, populate_from='title'),
        ),
    ]
