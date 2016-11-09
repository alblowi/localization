from __future__ import unicode_literals

from django.db import models
from buildingManager.models import Buildings, Floors

class systemLogs(models.Model):
    SysLogID = models.AutoField(primary_key=True)
    SysLogBuildingIDFK = models.ForeignKey(Buildings, blank=True, null=True)
    SysLogFloorIDFK = models.ForeignKey(Floors, blank=True, null=True)
    SysLogMACAddress = models.CharField(max_length=30, blank=True)
    SysLogRSSI = models.CharField(max_length=10, blank=False)
    SysLogLongitude = models.CharField(max_length=50, blank=True, null=True)
    SysLogLatitude = models.CharField(max_length=50, blank=True, null=True)
    SysLogTimestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

