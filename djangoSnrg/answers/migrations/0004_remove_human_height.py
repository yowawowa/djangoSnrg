# Generated by Django 4.2 on 2023-05-09 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0003_human_date_of_birth_alter_human_height'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='height',
        ),
    ]
