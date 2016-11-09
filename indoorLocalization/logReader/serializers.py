from rest_framework import serializers
from .models import systemLogs
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

User = get_user_model()

class systemLogsSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = systemLogs
        fields = ('SysLogID', 'SysLogBuildingIDFK', 'SysLogFloorIDFK', 'SysLogMACAddress', 'SysLogRSSI',
                  'SysLogLongitude', 'SysLogLatitude', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('log-detail', kwargs={'pk': obj.pk}, request= request)
        }