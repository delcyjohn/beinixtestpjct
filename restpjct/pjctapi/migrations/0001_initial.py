# Generated by Django 2.2.3 on 2019-08-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event', models.CharField(max_length=80)),
                ('Actor', models.CharField(max_length=20)),
            ],
        ),
    ]
