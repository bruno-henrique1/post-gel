# Generated by Django 5.0.4 on 2024-04-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postt', '0002_rename_category_categoryy_alter_categoryy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('is_published', models.BooleanField(default=False, help_text='Este campo precisará estar marcado para a página ser exibida publicamente.')),
                ('content', models.TextField()),
            ],
        ),
    ]
