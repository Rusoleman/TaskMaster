# Generated by Django 3.2.5 on 2021-07-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('cards', '0002_alter_card_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='limit_date',
            new_name='deadline',
        ),
        migrations.AddField(
            model_name='card',
            name='manager',
            field=models.ManyToManyField(blank=True, related_name='cards_member_manager', to='members.Member'),
        ),
    ]
