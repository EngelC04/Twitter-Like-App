# Generated by Django 2.2 on 2020-08-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
