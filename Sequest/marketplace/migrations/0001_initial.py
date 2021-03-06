# Generated by Django 2.1.2 on 2018-11-23 12:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HideRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm_message', models.TextField(max_length=5000)),
                ('pm_created_at', models.DateTimeField(auto_now_add=True)),
                ('pm_updated_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_reported', models.BooleanField(default=False)),
                ('offer_slug', models.SlugField(unique=True)),
                ('offer_price', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfferMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='documents/')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offermedias', to='marketplace.Offer')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField(max_length=4000)),
                ('category', models.IntegerField(choices=[(1, 'Video'), (2, 'Photo'), (3, 'Text')], default=1)),
                ('request_slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_reported', models.BooleanField(default=False)),
                ('anonymous', models.BooleanField(default=True)),
                ('start_price', models.IntegerField(validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='marketplace.Request'),
        ),
        migrations.AddField(
            model_name='offer',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messages',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='marketplace.Offer'),
        ),
        migrations.AddField(
            model_name='messages',
            name='pm_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messages',
            name='pm_updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hiderequests',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hiddenRequests', to='marketplace.Request'),
        ),
    ]
