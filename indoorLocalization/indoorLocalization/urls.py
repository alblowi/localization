"""indoorLocalization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from buildingManager.views import campusesViewSet, buildingViewSet, floorsViewSet, POIViewSet
from logParser.views import LogParserViewSet
from logReader.views import systemLogViewSet

Router = DefaultRouter()
Router.register('campuses', campusesViewSet)
Router.register('buildings', buildingViewSet)
Router.register('floors', floorsViewSet)
Router.register('poi', POIViewSet)
Router.register('parser', LogParserViewSet)
Router.register('reader', systemLogViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'api/v1/', include(Router.urls)),
]
