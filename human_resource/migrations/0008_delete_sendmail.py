# Generated by Django 4.0.6 on 2022-10-12 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0007_remove_sendmail_users_sendmail_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SendMail',
        ),
    ]
