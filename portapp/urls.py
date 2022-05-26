from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.portfolio_home,name='welcome'),
    url(r'^projects/$', views.project, name='project')
]