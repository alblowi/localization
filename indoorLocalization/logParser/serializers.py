from rest_framework import serializers
from .models import LogParser
from rest_framework.reverse import reverse

class LogParserSerializer(serializers.HyperlinkedModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = LogParser
        fields = ('LogFileID','LogFileDate', 'LogFileName', 'LogFileParsed', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('logparser-detail', kwargs={'pk': obj.pk}, request=request)
        }