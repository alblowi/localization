from rest_framework import serializers
from .models import Buildings, Floors, Campuses, PointOfInterests
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

User = get_user_model()

class CampusesSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Campuses
        fields = ('CampusID', 'CampusName', 'CampusAlias', 'CampusAddress', 'CampusLongitude', 'CampusLatitude',
                  'Active', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('campuses-detail', kwargs={'pk': obj.pk}, request= request)
        }

class BuildingsSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    Campuses = CampusesSerializer

    class Meta:
        model = Buildings
        fields = ('BuildingID', 'CampusIDFK', 'BuildingName', 'BuildingAlias', 'BuildingAddress', 'BuildingLongitude',
                  'BuildingLatitude', 'Active', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('buildings-detail', kwargs={'pk': obj.pk}, request= request)
        }

class FloorSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    Buildings = BuildingsSerializer

    class Meta:
        model = Floors
        fields = ('FloorID', 'BuildingIDFK', 'FloorNumber', 'FloorMAP', 'FloorAlias', 'links', 'credit')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('floors-detail', kwargs={'pk': obj.pk}, request= request)
        }



class POISerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    Floors = FloorSerializer

    class Meta:
        model = PointOfInterests
        fields = ('POIID', 'FloorIDFK', 'POIAlias', 'POILongitude', 'POILatitude', 'Active', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('pointofinterests-detail', kwargs={'pk': obj.pk}, request=request)
        }

class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links')


    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request= request)
        }