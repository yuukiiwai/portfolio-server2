# Generated by Django 4.1.5 on 2023-01-19 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_rename_abst_strongs_strong'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strong', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StrongExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(max_length=50)),
                ('strong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exps', to='index.strong')),
            ],
        ),
        migrations.DeleteModel(
            name='strong_exps',
        ),
        migrations.DeleteModel(
            name='Strongs',
        ),
    ]