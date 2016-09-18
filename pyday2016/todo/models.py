# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.encoding import smart_unicode


class Categoria(models.Model):
    nombre = models.CharField(max_length=64)

    def __unicode__(self):
        return smart_unicode(self.nombre)

    class Meta:
        verbose_name_plural = u"Categorías"


class Tarea(models.Model):
    nombre = models.CharField(max_length=64)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    categorias = models.ManyToManyField(Categoria,
                                        related_name="tareas")
    hecha = models.BooleanField(default=False)

    def __unicode__(self):
        return smart_unicode(self.nombre)

    class Meta:
        verbose_name_plural = u"Tareas"
