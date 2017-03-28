from django.conf.urls import url

from . import views

app_name = 'karty'
urlpatterns = [
        url(r'^$', views.MenuCardList.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.MenuCardDetail.as_view(), name='detail'),
        url(r'^api/$', views.APIMenuCardList.as_view(), name='api_index'),
        url(r'^api/(?P<menucard_id>[0-9]+)/$', views.APIMenuCardDetail.as_view(), name='api_detail'),
        ]
