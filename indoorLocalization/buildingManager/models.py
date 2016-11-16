from __future__ import unicode_literals

from django.db import models


class Campuses(models.Model):
    CampusID = models.AutoField(primary_key=True)
    CampusName = models.CharField(max_length=255, blank=False)
    CampusAlias = models.CharField(max_length=255, blank=True)
    CampusAddress = models.CharField(max_length=255, blank=False)
    CampusLongitude = models.CharField(max_length=50, blank=True)
    CampusLatitude = models.CharField(max_length=50, blank=True)
    Active = models.SmallIntegerField(blank=False, default=0)

    def __str__(self):
        return self.CampusName


class Buildings(models.Model):
    BuildingID = models.AutoField(primary_key=True)
    CampusIDFK = models.ForeignKey(Campuses, related_name='buildings')
    BuildingName = models.CharField(max_length=255, blank=False)
    BuildingAlias = models.CharField(max_length=255, blank=True)
    BuildingAddress = models.CharField(max_length=255, blank=False)
    BuildingLongitude = models.CharField(max_length=50, blank=True)
    BuildingLatitude = models.CharField(max_length=50, blank=True)
    Active = models.SmallIntegerField(blank=False, default=0)

    def __str__(self):
        return self.BuildingName


class Floors(models.Model):
    FloorID = models.AutoField(primary_key=True)
    BuildingIDFK = models.ForeignKey(Buildings, related_name='floors')
    FloorNumber = models.CharField(max_length=30, blank=False)
    FloorMAP = models.FileField(upload_to="./buildingManager/maps/")
    FloorAlias = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.FloorNumber


class PointOfInterests(models.Model):
    POIID = models.AutoField(primary_key=True)
    FloorIDFK = models.ForeignKey(Floors, related_name='poi')
    POIAlias = models.CharField(max_length=255, blank=True)
    POILongitude = models.CharField(max_length=50, blank=True)
    POILatitude = models.CharField(max_length=50, blank=True)
    Active = models.SmallIntegerField(blank=False, default=0)

    def __str__(self):
        return self.POIAlias
