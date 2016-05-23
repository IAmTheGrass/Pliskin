from django.conf.urls import url
from codes.views import Index, Create
from codes import views


urlpatterns = [
    url(r'^index/', Index.as_view()),
    url(r'^new/', Create.as_view(success_url="#")),
    url(r'^(?P<codes_id>\d+)/show/$', views.show, name='show'),
    url(r'^(?P<codes_id>\d+)/delete/$', views.delete, name='delete'),
]