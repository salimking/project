# Generated by Django 2.2.7 on 2019-11-24 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('license_id', models.CharField(blank=True, max_length=30)),
                ('type', models.CharField(blank=True, choices=[('S', 'Shop'), ('C', 'Company')], max_length=1)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inst_profile',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.Profile')),
                ('line1', models.CharField(max_length=50)),
                ('line2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('contactno', models.IntegerField()),
                ('email', models.EmailField(max_length=20)),
            ],
            options={
                'db_table': 'address',
            },
        ),
    ]