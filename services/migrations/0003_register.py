# Generated by Django 4.2.2 on 2023-07-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services2_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=111)),
                ('email', models.EmailField(max_length=111)),
                ('birth', models.CharField(max_length=33)),
                ('registerdate', models.CharField(max_length=44)),
                ('registertime', models.CharField(max_length=41)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
