# Generated by Django 2.2.6 on 2019-10-07 10:47

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
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('sent_at', models.DateField(auto_now=True)),
                ('message', models.CharField(max_length=256)),
                ('read', models.BooleanField(default=False)),
                ('read_at', models.DateTimeField(default=None, null=True)),
                ('notification_type', models.CharField(choices=[('REFILL', 'Refill shopping list budget'), ('BELOW THRESHOLD', 'Budget below set threshold'), ('BUDGET UPDATED', 'Budget updated')], max_length=20)),  # noqa
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),  # noqa
            ],
        ),
    ]