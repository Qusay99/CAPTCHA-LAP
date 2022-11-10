# Generated by Django 4.0 on 2022-01-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_alter_content_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='topic',
            field=models.CharField(choices=[('Mathe', 'Mathe'), ('Programmieren', 'Programmieren'), ('Volkswirtschaftslehre', 'Volkswirtschaftslehre'), ('Data Science', 'Data Science'), ('Informatik', 'Informatik'), ('Datenbanken', 'Datenbanken'), ('Recht', 'Recht'), ('Management', 'Management')], default='Mathe', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='topic',
            field=models.CharField(choices=[('Mathe', 'Mathe'), ('Programmieren', 'Programmieren'), ('Volkswirtschaftslehre', 'Volkswirtschaftslehre'), ('Data Science', 'Data Science'), ('Informatik', 'Informatik'), ('Datenbanken', 'Datenbanken'), ('Recht', 'Recht'), ('Management', 'Management')], default='Mathe', max_length=50),
        ),
    ]
