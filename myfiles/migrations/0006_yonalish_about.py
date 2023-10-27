# Generated by Django 4.2.6 on 2023-10-25 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('data', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('yonalish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.yonalish')),
            ],
        ),
    ]