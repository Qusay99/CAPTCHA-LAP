# Generated by Django 4.0 on 2022-01-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_document_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
    ]