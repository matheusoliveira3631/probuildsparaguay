# Generated by Django 3.0.2 on 2020-01-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeao',
            name='miniatura',
            field=models.ImageField(default='errorImg.png', upload_to=None),
        ),
    ]