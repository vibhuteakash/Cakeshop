# Generated by Django 4.0.3 on 2022-08-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=10)),
                ('cvv', models.CharField(max_length=4)),
                ('balance', models.FloatField(default=10000)),
            ],
            options={
                'db_table': 'Payments',
            },
        ),
    ]