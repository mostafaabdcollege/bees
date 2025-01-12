# Generated by Django 5.1.4 on 2025-01-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='ville',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'prof'), (3, 'student')], default=2),
        ),
    ]
