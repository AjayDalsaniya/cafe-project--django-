# Generated by Django 4.1.3 on 2022-12-13 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0007_alter_user_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='restaurant_idrestaurant',
            new_name='idrestaurant',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='area_pincode',
            new_name='pincode',
        ),
    ]
