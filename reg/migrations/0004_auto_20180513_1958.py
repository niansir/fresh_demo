# Generated by Django 2.0.4 on 2018-05-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_auto_20180513_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
