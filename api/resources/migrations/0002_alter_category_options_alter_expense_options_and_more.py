# Generated by Django 4.1.1 on 2022-09-14 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={},
        ),
        migrations.RemoveField(
            model_name='expense',
            name='category_id',
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='resources.category'),
        ),
    ]
