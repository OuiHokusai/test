# Generated by Django 2.1.4 on 2019-02-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sschool', models.CharField(max_length=20)),
                ('spro', models.CharField(max_length=30)),
            ],
        ),
    ]
