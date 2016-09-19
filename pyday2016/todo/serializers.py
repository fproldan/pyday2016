# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Categoria, Tarea


class TareaListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(usuario=self.context['request'].user)
        return super(TareaListSerializer, self).to_representation(data)


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
        list_serializer_class = TareaListSerializer
        fields = ('id', 'nombre', 'usuario',
                  'categorias', 'hecha', 'url')


class CategoriaSerializer(serializers.ModelSerializer):
    tareas = TareaSerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(
        'categoria-detail',
        source='id',
        read_only=True)

    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'url', 'tareas')
