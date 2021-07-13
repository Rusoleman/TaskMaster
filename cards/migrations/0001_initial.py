# Generated by Django 3.2.5 on 2021-07-11 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Card', max_length=40)),
                ('description', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField()),
                ('limit_date', models.DateTimeField()),
                ('position', models.IntegerField()),
                ('list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.list')),
                ('member', models.ManyToManyField(related_name='cards_member', to='members.Member')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
