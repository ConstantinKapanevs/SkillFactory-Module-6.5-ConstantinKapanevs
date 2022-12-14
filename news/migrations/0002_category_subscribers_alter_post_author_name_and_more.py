# Generated by Django 4.1.1 on 2022-10-28 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to='news.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('news', 'Новость'), ('article', 'Статья')], default='news', max_length=8, verbose_name='Тип поста'),
        ),
    ]
