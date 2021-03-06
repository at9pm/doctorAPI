# Generated by Django 3.1 on 2021-05-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorlistAPI', '0003_rename_district_language_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctorID',
            field=models.CharField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together={('doctor', 'language')},
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('doctor', 'serviceType')},
        ),
    ]
