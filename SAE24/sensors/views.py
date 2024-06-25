from django.shortcuts import render
from .models import Sensor, SensorData

def index(request):
    sensors = Sensor.objects.all()
    return render(request, 'sensors/index.html', {'sensors': sensors})

def sensor_detail(request, sensor_id):
    sensor = Sensor.objects.get(pk=sensor_id)
    data = SensorData.objects.filter(sensor=sensor)
    return render(request, 'sensors/sensor_detail.html', {'sensor': sensor, 'data': data})
