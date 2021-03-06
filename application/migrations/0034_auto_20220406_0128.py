# Generated by Django 3.2.8 on 2022-04-06 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0033_alter_module_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='user',
        ),
        migrations.RemoveField(
            model_name='learning',
            name='bookmark',
        ),
        migrations.RemoveField(
            model_name='learning',
            name='term',
        ),
        migrations.RemoveField(
            model_name='learning',
            name='user',
        ),
        migrations.RemoveField(
            model_name='term',
            name='category',
        ),
        migrations.RemoveField(
            model_name='term',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='term',
            name='topics',
        ),
        migrations.RemoveField(
            model_name='term',
            name='user',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
        migrations.DeleteModel(
            name='Learning',
        ),
        migrations.DeleteModel(
            name='Term',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
