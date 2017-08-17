from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


from .views import TweetListView, TweetDetailView


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet/
    #url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
