# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TareaViewSet

router = DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'tarea', TareaViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]
