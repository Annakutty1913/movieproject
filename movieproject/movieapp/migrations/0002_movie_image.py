# Generated by Django 4.1 on 2022-09-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='gygh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
