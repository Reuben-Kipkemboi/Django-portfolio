from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.portfolio_home,name='welcome'),
    url(r'^projects/$', views.project, name='project'),
    url(r'^my-certifications/$', views.certifications, name='certificate')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)