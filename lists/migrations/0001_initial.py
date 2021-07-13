# Generated by Django 3.2.5 on 2021-07-11 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New List', max_length=40)),
                ('creation_date', models.DateTimeField()),
                ('position', models.IntegerField()),
                ('boards', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='boards.board')),
            ],
        ),
    ]
