# Generated by Django 2.2.12 on 2020-04-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agileprinciples',
            name='definitions',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='agilevalues',
            name='definitions',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
