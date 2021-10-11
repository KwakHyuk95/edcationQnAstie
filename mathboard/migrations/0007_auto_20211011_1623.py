# Generated by Django 3.1.3 on 2021-10-11 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mathboard', '0006_auto_20211001_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathanswer',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_mathanswer', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mathanswer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mathanswer',
            name='voter',
            field=models.ManyToManyField(related_name='voter_mathanswer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mathquestion',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_mathquestion', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mathquestion',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mathquestion',
            name='voter',
            field=models.ManyToManyField(related_name='voter_mathquestion', to=settings.AUTH_USER_MODEL),
        ),
    ]