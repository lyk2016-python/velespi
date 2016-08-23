"""velespi URL Configuration

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
from django.conf import settings
from django.views.static import serve
from places.views import (
    index, detail, new_place, new_media, new_review,
    like_place
)
from profiles.views import register, login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^register$', register, name="register"),
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^places/(?P<id>\d+)$', detail, name='place_detail'),
    url(r'^places/(?P<place_id>\d+)/new-media$', new_media, name='new_media'),
    url(r'^places/(?P<place_id>\d+)/new-review$', new_review, name='new_review'),
    url(r'^places/(?P<place_id>\d+)/like$', like_place, name='like_place'),
    url(r'^new-place$', new_place, name="new_place"),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
