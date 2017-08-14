from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


from .views import tweet_detail_view, tweet_list_view


urlpatterns = [
    url(r'^$', tweet_list_view, name='list'),
    url(r'^1/$', tweet_detail_view, name='detail'),
]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
