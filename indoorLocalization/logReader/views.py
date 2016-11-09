from rest_framework import viewsets, authentication, permissions

from .models import systemLogs
from .serializers import systemLogsSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class systemLogViewSet(viewsets.ModelViewSet):
    queryset = systemLogs.objects.all()
    serializer_class = systemLogsSerializer
