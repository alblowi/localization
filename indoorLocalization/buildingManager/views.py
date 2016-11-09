from rest_framework import viewsets, authentication, permissions

from .models import Campuses, Buildings, Floors, PointOfInterests
from .serializers import CampusesSerializer, BuildingsSerializer, FloorSerializer, POISerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class campusesViewSet(viewsets.ModelViewSet):
    queryset = Campuses.objects.all()
    serializer_class = CampusesSerializer

class buildingViewSet(viewsets.ModelViewSet):
    queryset = Buildings.objects.all()
    serializer_class = BuildingsSerializer

class floorsViewSet(viewsets.ModelViewSet):
    queryset = Floors.objects.all()
    serializer_class = FloorSerializer

class POIViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterests.objects.all()
    serializer_class = POISerializer
