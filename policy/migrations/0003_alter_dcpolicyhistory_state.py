# Generated by Django 3.2 on 2022-02-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0002_alter_dcpolicy_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcpolicyhistory',
            name='state',
            field=models.CharField(blank=True, choices=[(0, 'New'), (1, 'Quoted'), (2, 'Active')], default=0, max_length=255, null=True, verbose_name='State'),
        ),
    ]
