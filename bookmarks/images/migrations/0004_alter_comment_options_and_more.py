# Generated by Django 4.1.13 on 2024-06-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created'], name='images_comm_created_03a2ea_idx'),
        ),
    ]
