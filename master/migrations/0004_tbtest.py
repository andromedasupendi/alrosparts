# Generated by Django 2.1.4 on 2020-01-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_tbcomponent'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testName', models.CharField(max_length=60)),
                ('testDesc', models.CharField(max_length=60)),
            ],
        ),
    ]