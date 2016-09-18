# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
import pyday2016.todo.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(pyday2016.todo.urls)),
]
