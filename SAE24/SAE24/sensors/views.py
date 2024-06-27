import csv
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sensor, SensorData
from .forms import SensorForm, SensorDataFilterForm

def index(request):
    sensors = Sensor.objects.all()
    return render(request, 'sensors/index.html', {'sensors': sensors})

def sensor_detail(request, id):
    sensor = get_object_or_404(Sensor, pk=id)
    data = SensorData.objects.filter(sensor=sensor)
    
    filter_form = SensorDataFilterForm(request.GET)
    if filter_form.is_valid():
        if filter_form.cleaned_data['start_date']:
            data = data.filter(timestamp__date__gte=filter_form.cleaned_data['start_date'])
        if filter_form.cleaned_data['end_date']:
            data = data.filter(timestamp__date__lte=filter_form.cleaned_data['end_date'])
        if filter_form.cleaned_data['min_temperature'] is not None:
            data = data.filter(temperature__gte=filter_form.cleaned_data['min_temperature'])
        if filter_form.cleaned_data['max_temperature'] is not None:
            data = data.filter(temperature__lte=filter_form.cleaned_data['max_temperature'])

    if request.method == 'POST':
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect('sensor_detail', id=sensor.id)
    else:
        form = SensorForm(instance=sensor)

    return render(request, 'sensors/sensor_detail.html', {'sensor': sensor, 'data': data, 'form': form, 'filter_form': filter_form})

def export_sensor_data_csv(request, id):
    sensor = get_object_or_404(Sensor, pk=id)
    data = SensorData.objects.filter(sensor=sensor)
    
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{sensor.name}_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Timestamp', 'Temperature'])
    
    for entry in data:
        writer.writerow([entry.timestamp, entry.temperature])

    return response