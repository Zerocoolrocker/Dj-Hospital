# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Personas.Persona')),
                ('habitacion', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
                ('diagnostico', models.CharField(max_length=1000000)),
            ],
            options={
            },
            bases=('Personas.persona',),
        ),
    ]
