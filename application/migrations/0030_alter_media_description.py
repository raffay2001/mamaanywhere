# Generated by Django 3.2.8 on 2022-03-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0029_alter_training_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(),
        ),
    ]
