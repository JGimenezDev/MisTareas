# Generated by Django 5.0.7 on 2024-08-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tareas", "0004_alter_tarea_fecha_alter_tarea_prioridad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarea",
            name="prioridad",
            field=models.CharField(
                blank=True,
                choices=[("0", "Baja"), ("1", "Media"), ("2", "Alta")],
                max_length=1,
                null=True,
            ),
        ),
    ]