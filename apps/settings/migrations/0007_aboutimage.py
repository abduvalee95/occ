# Generated by Django 4.0.4 on 2022-05-02 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='movie_image/')),
                ('history', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_image', to='settings.about')),
            ],
            options={
                'verbose_name': 'Картинка истории',
                'verbose_name_plural': 'Картинки историй',
            },
        ),
    ]