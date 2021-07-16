# Generated by Django 3.2.5 on 2021-07-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('boards', '0002_board_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='boards_member', to='members.Member'),
        ),
    ]
