# Generated by Django 3.2 on 2022-02-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0004_alter_dcpolicyhistory_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcpolicyhistory',
            name='state',
            field=models.CharField(blank=True, choices=[('new', 'New'), ('quoted', 'Quoted'), ('active', 'Active')], default='new', max_length=255, null=True, verbose_name='State'),
        ),
    ]
