# Generated by Django 3.0.8 on 2020-12-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credicxo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup_info',
            name='email',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
