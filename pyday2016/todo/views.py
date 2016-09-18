# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Categoria, Tarea
from .serializers import CategoriaSerializer, TareaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

