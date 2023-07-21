# Generated by Django 4.2.2 on 2023-06-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=3000)),
                ('book_available', models.BooleanField()),
            ],
        ),
    ]
