# Generated by Django 3.0.4 on 2020-07-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('Graduation_year', models.CharField(max_length=50)),
            ],
        ),
    ]
