# Generated by Django 2.1.5 on 2019-04-06 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0008_auto_20190405_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
            preserve_default=False,
        ),
    ]
