from django.conf.urls import url

from . import views
app_name = 'home'

urlpatterns = [
    url(r'^', views.home, name='home'),
    #url(r'^send_command/(?P<box>[\w\-]+)/(?P<code>[\w\-]+)/$', views.send_command, name='send_commmand'),
]