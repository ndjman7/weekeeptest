from django.conf.urls import url
from . import views

app_name = 'wkcalendar'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^1$', views.index2, name='index2'),
    url('^popup$', views.popup, name='popup'),
    url('^add_schedule$', views.add_schedule, name='add_schedule'),
]
