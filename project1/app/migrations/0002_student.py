# Generated by Django 5.0.3 on 2024-04-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdname', models.CharField(max_length=50)),
                ('stdage', models.IntegerField()),
            ],
        ),
    ]
