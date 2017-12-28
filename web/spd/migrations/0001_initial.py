# Generated by Django 2.0 on 2017-12-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('standardized_content', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
    ]