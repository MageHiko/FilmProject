# Generated by Django 4.2.3 on 2023-07-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(max_length=256)),
                ('about', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='actor_images/')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='FilmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('rating', models.FloatField(default=0)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=256, null=True)),
                ('country', models.CharField(max_length=256)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='postery/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('fragman', models.FileField(blank=True, null=True, upload_to='fragmans/')),
                ('views_count', models.IntegerField(default=0)),
                ('about', models.TextField(blank=True, null=True)),
                ('actors', models.ManyToManyField(related_name='films', to='film.actormodel')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
                'ordering': ('-id',),
            },
        ),
    ]
