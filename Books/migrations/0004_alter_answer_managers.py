# Generated by Django 4.0.4 on 2022-06-10 02:05

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_answer_third_option'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='answer',
            managers=[
                ('my_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
