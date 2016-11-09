from rest_framework.routers import DefaultRouter

from . import views

LogReaderRouter = DefaultRouter()
LogReaderRouter.register(r'systemLogs', views.systemLogViewSet)