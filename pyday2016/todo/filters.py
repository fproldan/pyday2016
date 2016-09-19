import django_filters
from django.contrib.auth import get_user_model
from .models import Tarea, Categoria


class TareaFilterSet(django_filters.FilterSet):

    usuario = django_filters.ModelChoiceFilter(
        to_field_name="username",
        queryset=get_user_model().objects.all())

    categorias = django_filters.ModelMultipleChoiceFilter(
        to_field_name="nombre",
        queryset=Categoria.objects.all())

    class Meta:
        model = Tarea
        fields = ('hecha', 'usuario', 'categorias')
