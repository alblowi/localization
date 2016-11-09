from rest_framework.routers import DefaultRouter

from . import views

BuildingManagerRouter = DefaultRouter()
BuildingManagerRouter.register(r'campuses', views.campusesViewSet)
BuildingManagerRouter.register(r'buildings', views.buildingViewSet)
BuildingManagerRouter.register(r'floors', views.floorsViewSet)
BuildingManagerRouter.register(r'pois', views.POIViewSet)
