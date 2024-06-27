from django.db import models


class SensorData(models.Model):
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'sensor_data'


class Sensor(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(unique=True, max_length=100)
    room = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        db_table = 'sensors'
