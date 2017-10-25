from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json

from .models import Data

def input(request):
    client_id = request.GET.get("client_Id", "0")
    temp = request.GET.get("temp", "0")
    hum = request.GET.get("hum", "0")
    soil = request.GET.get("soil", "0")
    light = request.GET.get("light", "0")
    
    data = Data.objects.create(client_id=client_id, temp=temp, hum=hum, soil=soil, light=light)
    data.publish()