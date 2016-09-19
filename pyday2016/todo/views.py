# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import DjangoFilterBackend
from .models import Categoria, Tarea
from .serializers import CategoriaSerializer, TareaSerializer
from .filters import TareaFilterSet


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = TareaFilterSet

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)
