# Generated by Django 4.2 on 2023-05-07 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_description', models.CharField(max_length=500)),
                ('project_img', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_img', models.FileField(upload_to='Project/images/')),
                ('project_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]
