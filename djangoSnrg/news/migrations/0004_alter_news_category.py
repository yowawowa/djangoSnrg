# Generated by Django 4.2 on 2023-05-04 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category'),
        ),
    ]
