# Generated by Django 3.1.7 on 2021-08-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=14)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
            ],
        ),
    ]