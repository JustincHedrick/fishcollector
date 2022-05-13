# Generated by Django 4.0.4 on 2022-05-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='River',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creeks', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('fish', models.TextField(max_length=100)),
            ],
        ),
    ]