# Generated by Django 4.1.3 on 2022-12-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_project_end_date_alter_project_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]