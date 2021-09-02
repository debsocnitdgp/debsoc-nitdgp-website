# Generated by Django 3.2.6 on 2021-08-30 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Debator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('college', models.CharField(max_length=100)),
                ('college_year', models.IntegerField(default='1')),
                ('discord_id', models.CharField(blank=True, max_length=100, null=True)),
                ('prior', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
    ]