# Generated by Django 2.1.15 on 2020-05-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0004_auto_20200528_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit',
            name='Address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='edit',
            name='Applicant_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='edit',
            name='CNIC',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='edit',
            name='Father_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='edit',
            name='Form_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='edit',
            name='Program',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='edit',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
