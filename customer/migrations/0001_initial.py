# Generated by Django 3.2 on 2022-02-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DcCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(db_index=True, max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]