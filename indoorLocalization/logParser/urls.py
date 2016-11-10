from rest_framework.routers import DefaultRouter

from . import views

LogParserRouter = DefaultRouter()
LogParserRouter.register(r'upload_parser', views.LogParserViewSet)
