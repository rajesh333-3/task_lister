# Generated by Django 4.0.3 on 2022-04-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_remove_todo_todo_id_todo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=75)),
                ('a_designation', models.CharField(choices=[('Trainee', 'Trainee'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('CEO', 'Ceo')], default='Trainee', max_length=75)),
                ('a_exp', models.IntegerField()),
            ],
        ),
    ]
