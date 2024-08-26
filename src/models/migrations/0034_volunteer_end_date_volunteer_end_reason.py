# Generated by Django 4.0.4 on 2024-08-11 00:44

from django.db import migrations, models


def set_default_values(apps, schema_editor):
    Volunteer = apps.get_model('models', 'volunteer')
    db_alias = schema_editor.connection.alias
   
    Volunteer.objects.update(active=True)

class Migration(migrations.Migration):

    dependencies = [
        ('models', '0033_alter_route_bonusroute'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='end_reason',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='active',
            field=models.BooleanField(default=True),
        ),  
        migrations.RunPython(set_default_values),
    ]
