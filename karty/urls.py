from django.conf.urls import url

from . import views

app_name = 'karty'
urlpatterns = [
        url(r'^$', views.menucard_list, name='index'),
        url(r'^card/(?P<menucard_id>[0-9]+)/$', views.menucard_detail, name='detail'),
        ]
