# -*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

import pyday2016.todo.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(pyday2016.todo.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
