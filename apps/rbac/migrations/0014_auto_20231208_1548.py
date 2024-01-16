# Generated by Django 4.1.10 on 2023-12-08 07:48

from django.db import migrations


def migrate_update_offline_usersession_permission_name(apps, *args):
    perm_model = apps.get_model('auth', 'Permission')
    perm_model.objects.filter(codename='offline_usersession').update(name='Offline user session')


class Migration(migrations.Migration):
    dependencies = [
        ('rbac', '0013_alter_menupermission_options'),
    ]

    operations = [
        migrations.RunPython(migrate_update_offline_usersession_permission_name)
    ]