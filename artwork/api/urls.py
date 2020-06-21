
from django.urls import path

from api.views import index, create_artwork

urlpatterns = [

    path('', index),
    path('create_artwork', create_artwork),
]

