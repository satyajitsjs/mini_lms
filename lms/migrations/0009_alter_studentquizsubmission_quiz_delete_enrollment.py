# Generated by Django 5.1.1 on 2024-09-27 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_alter_studentquizsubmission_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentquizsubmission',
            name='quiz',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.quiz'),
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]
