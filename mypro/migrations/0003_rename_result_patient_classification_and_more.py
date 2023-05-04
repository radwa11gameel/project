# Generated by Django 4.2 on 2023-04-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypro', '0002_alter_patient_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='result',
            new_name='classification',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='medical_license_number',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='patients',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialty',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='allergies',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='conditions',
        ),
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='prediction',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]