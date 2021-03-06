# Generated by Django 2.1.4 on 2019-04-10 16:56

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
            name='BdcProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bdc_name', models.CharField(max_length=150, verbose_name='BDC Name')),
                ('bdc_short_name', models.CharField(max_length=20, unique=True, verbose_name='Short Name')),
                ('phone', models.CharField(max_length=16, unique=True)),
                ('address', models.TextField(verbose_name='Office Address')),
                ('contactp', models.CharField(max_length=150, verbose_name='Contact Person')),
                ('bdc_logo', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BdcStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss', models.BooleanField(default=False, editable=False)),
                ('bdc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.BdcProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
