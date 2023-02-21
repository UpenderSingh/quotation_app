# Generated by Django 4.1.5 on 2023-02-20 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('quantity', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quote_expiry_date', models.DateTimeField()),
                ('total', models.CharField(max_length=50)),
                ('sub_total', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customerapp.customerprofile')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotationapp.item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]