# Generated by Django 3.0.4 on 2020-07-10 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200707_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('years', models.CharField(max_length=50)),
                ('tools', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
