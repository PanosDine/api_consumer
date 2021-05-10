import os
import requests
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Launch


def get_launches(request):
    url = 'https://api.spacexdata.com/v3/launches'
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    launches = response.json()
    return launches
    


