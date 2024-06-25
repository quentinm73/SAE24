from django.db import models

class Sensor(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.sensor.name} at {self.timestamp}"
