# Generated by Django 2.0.4 on 2018-05-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uphone',
            field=models.BigIntegerField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='uregister_time',
            field=models.DateTimeField(),
        ),
    ]
