# Generated by Django 4.0.2 on 2022-02-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicschedule',
            name='music_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='musicschedule',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to='./media/music'),
        ),
    ]
