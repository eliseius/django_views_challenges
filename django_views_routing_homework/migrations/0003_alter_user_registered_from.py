# Generated by Django 4.2.3 on 2023-10-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_views_routing_homework', '0002_alter_user_options_user_full_name_gte_5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registered_from',
            field=models.CharField(choices=[('wb', 'website'), ('m_ap', 'mobile_app')], default='wb', max_length=120),
        ),
    ]
