# Generated by Django 2.0.4 on 2018-05-13 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_auto_20180513_1958'),
        ('goods', '0002_auto_20180513_0124'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='carttable',
        ),
    ]
