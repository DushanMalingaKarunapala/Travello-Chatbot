# Generated by Django 4.2.1 on 2023-05-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='besttouristattractions',
            name='location',
        ),
        migrations.RemoveField(
            model_name='campingsites',
            name='location',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='location',
        ),
        migrations.RemoveField(
            model_name='conservationforests',
            name='location',
        ),
        migrations.RemoveField(
            model_name='factories',
            name='location',
        ),
        migrations.RemoveField(
            model_name='farms',
            name='location',
        ),
        migrations.RemoveField(
            model_name='gardens',
            name='location',
        ),
        migrations.RemoveField(
            model_name='hikingareas',
            name='location',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='location',
        ),
        migrations.RemoveField(
            model_name='lakes_reservors',
            name='location',
        ),
        migrations.RemoveField(
            model_name='mountainpeaks',
            name='location',
        ),
        migrations.RemoveField(
            model_name='nationalparks',
            name='location',
        ),
        migrations.RemoveField(
            model_name='parks',
            name='location',
        ),
        migrations.RemoveField(
            model_name='religious_places',
            name='location',
        ),
        migrations.RemoveField(
            model_name='restaurants',
            name='location',
        ),
        migrations.RemoveField(
            model_name='waterfalls',
            name='location',
        ),
        migrations.AddField(
            model_name='besttouristattractions',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='besttouristattractions',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campingsites',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campingsites',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cities',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cities',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conservationforests',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conservationforests',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factories',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factories',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farms',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farms',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardens',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardens',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hikingareas',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hikingareas',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotels',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotels',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lakes_reservors',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lakes_reservors',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mountainpeaks',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mountainpeaks',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nationalparks',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nationalparks',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parks',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parks',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='religious_places',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='religious_places',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurants',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurants',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterfalls',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterfalls',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
