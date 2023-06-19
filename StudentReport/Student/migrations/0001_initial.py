# Generated by Django 4.1.7 on 2023-06-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('age', models.IntegerField(null=True)),
                ('major', models.CharField(max_length=6, null=True)),
            ],
        ),
    ]