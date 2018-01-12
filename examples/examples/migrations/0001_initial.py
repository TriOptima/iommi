# Generated by Django 2.0.1 on 2018-01-12 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('a', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bar',
            name='b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examples.Foo'),
        ),
    ]
