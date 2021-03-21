# Generated by Django 3.0.5 on 2021-03-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('info_url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
