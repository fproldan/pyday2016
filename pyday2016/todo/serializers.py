# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Categoria, Tarea


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')


class TareaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        'tarea-detail',
        source='id',
        read_only=True)

    usuario = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault())

    categorias = serializers.SlugRelatedField(
        slug_field="nombre",
        queryset=Categoria.objects.all(),
        many=True)

    class Meta:
        model = Tarea
        fields = ('id', 'nombre', 'usuario',
                  'categorias', 'hecha', 'url')
