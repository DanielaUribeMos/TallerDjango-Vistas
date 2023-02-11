from measurements.models import Measurement
from variables.models import Variable
from datetime import datetime

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    variable2=Variable.objects.get(pk=new_var["variable"])
    measurement = get_measurement(var_pk)
    measurement.variable=variable2
    measurement.value=new_var["value"]
    measurement.unit=new_var["unit"]
    measurement.place=new_var["place"]
    dateTimeInFormat=datetime.strptime(new_var["dateTime"], '%Y-%m-%dT%H:%M:%S.%fZ')
    measurement.dateTime=dateTimeInFormat
    measurement.save()
    return measurement

def create_measurement(var):
    variable2=Variable.objects.get(pk=var["variable"])
    measurement = Measurement(variable=variable2, value=var["value"], unit=var["unit"], place=var["place"], dateTime=var["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement = get_measurement(var_pk)
    measurement.delete()
    return