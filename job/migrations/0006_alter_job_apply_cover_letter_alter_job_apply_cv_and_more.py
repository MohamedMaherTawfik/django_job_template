# Generated by Django 4.2.6 on 2023-11-07 21:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_job_apply_cover_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_apply',
            name='cover_letter',
            field=models.TextField(help_text='Add your Notes Here...', max_length=400),
        ),
        migrations.AlterField(
            model_name='job_apply',
            name='cv',
            field=models.FileField(help_text='Please Enter Your latest CV', upload_to='cv', validators=[django.core.validators.FileExtensionValidator(['pdf'], message='Only PDF files are allowed.')]),
        ),
        migrations.AlterField(
            model_name='job_apply',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_apply', to='job.job'),
        ),
    ]
