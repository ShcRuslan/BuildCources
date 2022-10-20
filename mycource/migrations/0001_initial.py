# Generated by Django 4.1.2 on 2022-10-17 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('imgpath', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='mycource.category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Phone'), (2, 'Facebook'), (3, 'Email')])),
                ('value', models.CharField(max_length=100)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='mycource.course')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='mycource.course')),
            ],
        ),
    ]
