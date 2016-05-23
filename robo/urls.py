from django.conf.urls import url
from robo.views import AboutView, Index, RoboCreate
from robo import views

urlpatterns = [
    url(r'^about/', AboutView.as_view()),
    url(r'^index/', Index.as_view()),
    url(r'^(?P<robo_id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^new/', RoboCreate.as_view(success_url="#")),
    url(r'^(?P<robo_id>\d+)/show/$', views.show, name='show'),
]