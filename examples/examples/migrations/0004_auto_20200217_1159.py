# Generated by Django 2.2.9 on 2020-02-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0003_tbar'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='tfoo',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]