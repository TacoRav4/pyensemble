# Generated by Django 2.2.7 on 2020-05-25 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyensemble', '0004_auto_20200525_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentxform',
            name='form_handler',
            field=models.CharField(blank=True, default='form_generic', max_length=50),
        ),
    ]
