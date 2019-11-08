# Generated by Django 2.2.7 on 2019-11-08 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('states', '0002_auto_20191106_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='date of event')),
                ('activity_type', models.CharField(choices=[('sports and recreation', 'sports and recreation'), ('education', 'education'), ('health', 'health'), ('food', 'food'), ('admin', 'admin'), ('work', 'work')], max_length=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.City')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]