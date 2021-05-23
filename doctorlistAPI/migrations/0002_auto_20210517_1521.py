# Generated by Django 3.2.3 on 2021-05-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorlistAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='contactNumber',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='district',
            field=models.CharField(choices=[('KL', 'Kowloon'), ('HK', 'Hong Kong'), ('IL', 'Island'), ('NT', 'New Territories')], max_length=2),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='openingHours',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
