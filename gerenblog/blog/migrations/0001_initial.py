# Generated by Django 2.0.7 on 2018-07-30 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('read_datails', models.IntegerField(default=0, verbose_name='阅读数量')),
                ('images', models.ImageField(default='', upload_to='blog/%Y/%m')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '博客具体信息',
                'verbose_name_plural': '博客具体信息',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='type_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogType', verbose_name='文章类型'),
        ),
    ]
