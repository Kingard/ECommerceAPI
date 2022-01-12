# Generated by Django 4.0.1 on 2022-01-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='author', max_length=70),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(),
        ),
    ]