# Generated by Django 5.0.2 on 2024-03-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=30)),
                ('Age', models.IntegerField(max_length=20)),
                ('DateOfBirth', models.DateField(max_length=10)),
            ],
        ),
    ]