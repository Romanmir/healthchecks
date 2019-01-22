# Generated by Django 2.1.5 on 2019-01-12 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20190112_1426'),
        ('api', '0053_check_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Project'),
        ),
        migrations.AddField(
            model_name='check',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Project'),
        ),
    ]