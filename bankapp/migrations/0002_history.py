# Generated by Django 3.0.5 on 2021-06-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('receiver', models.CharField(max_length=50)),
                ('transfer', models.CharField(max_length=50)),
            ],
        ),
    ]
