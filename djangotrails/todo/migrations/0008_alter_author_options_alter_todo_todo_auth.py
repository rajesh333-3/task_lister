# Generated by Django 4.0.3 on 2022-04-04 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': "Author's"},
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.author'),
        ),
    ]
