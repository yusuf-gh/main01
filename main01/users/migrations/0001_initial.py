# Generated by Django 5.0.1 on 2024-01-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]