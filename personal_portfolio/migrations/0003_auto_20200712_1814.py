# Generated by Django 3.0.7 on 2020-07-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_portfolio', '0002_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]