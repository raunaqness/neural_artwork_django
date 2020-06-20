from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response

# Create your views here.

@api_view(('GET',))
def index(request):
    return Response('Hello world!')
