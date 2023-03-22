# Generated by Django 4.1.7 on 2023-03-15 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Author Name')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag Name')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Music Name')),
                ('url', models.URLField(blank=True, verbose_name='Music Youtube URL')),
                ('author', models.ForeignKey(on_delete=models.SET('Deleted'), to='music_module.author')),
                ('tags', models.ManyToManyField(related_name='musics', to='music_module.tag', verbose_name='Music Tags')),
            ],
        ),
    ]