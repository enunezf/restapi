from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/$', views.tipos_atributos_list),
    url(r'^api/(?P<pk>[0-9]+)/$', views.tipos_atributos_detail),
]