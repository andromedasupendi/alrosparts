# Generated by Django 2.1.4 on 2020-01-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbProjekte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projTitle', models.CharField(max_length=200)),
                ('projDesc', models.TextField()),
                ('projCreated', models.DateTimeField(auto_now_add=True)),
                ('projAuthor', models.CharField(max_length=60)),
            ],
        ),
    ]