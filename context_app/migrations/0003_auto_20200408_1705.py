# Generated by Django 2.2.12 on 2020-04-08 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('context_app', '0002_auto_20200408_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agileprinciples',
            options={'verbose_name': 'Agile Principle', 'verbose_name_plural': 'Agile Principles'},
        ),
        migrations.AlterModelOptions(
            name='agilevalues',
            options={'verbose_name': 'Agile Value', 'verbose_name_plural': 'Agile Values'},
        ),
    ]