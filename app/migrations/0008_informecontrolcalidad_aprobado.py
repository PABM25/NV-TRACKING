from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_barco_lugardestino'),
    ]

    operations = [
        migrations.AddField(
            model_name='informecontrolcalidad',
            name='aprobado',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
