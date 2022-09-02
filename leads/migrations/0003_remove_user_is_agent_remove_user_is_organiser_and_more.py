# Generated by Django 4.1 on 2022-09-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_user_is_agent_user_is_organiser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_agent',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_organiser',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('A', 'Agent'), ('O', 'Organiser')], default='O', max_length=1),
            preserve_default=False,
        ),
    ]