# Generated by Django 4.2 on 2023-05-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
