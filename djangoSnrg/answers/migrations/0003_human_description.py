# Generated by Django 4.2.5 on 2023-09-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_alter_human_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]