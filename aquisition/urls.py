from django.conf.urls import url
from aquisition.views import Index, Create
from aquisition import views


urlpatterns = [
    url(r'^index/', Index.as_view()),
    url(r'^new/', Create.as_view(success_url="#")),
    url(r'^(?P<aquisition_id>\d+)/show/$', views.show, name='show'),
    url(r'^(?P<aquisition_id>\d+)/delete/$', views.delete, name='delete'),
]