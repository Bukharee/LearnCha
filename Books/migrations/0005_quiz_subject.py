# Generated by Django 4.0.4 on 2022-06-10 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_alter_answer_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Books.subject'),
            preserve_default=False,
        ),
    ]
