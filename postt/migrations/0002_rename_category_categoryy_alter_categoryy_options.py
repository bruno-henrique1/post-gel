# Generated by Django 5.0.4 on 2024-04-23 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postt', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoryy',
        ),
        migrations.AlterModelOptions(
            name='categoryy',
            options={'verbose_name': 'Categoryy', 'verbose_name_plural': 'Categoriess'},
        ),
    ]
