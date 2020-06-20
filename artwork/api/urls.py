
from django.urls import path

from api.views import index, create_artwork

urlpatterns = [

    path('', index),
    path('artwork', create_artwork),
]

