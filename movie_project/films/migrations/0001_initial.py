# Generated by Django 5.1.3 on 2024-11-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('film_content', models.TextField(verbose_name='Краткое содержание')),
                ('review', models.TextField(verbose_name='Отзыв')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]