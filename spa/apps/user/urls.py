from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from spa.apps.user import views

urlpatterns = \
    patterns('',
             url(r'^user/$', views.UserList.as_view(), name='user-list'),
             url(r'^user/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='user-detail')
)

urlpatterns = format_suffix_patterns(urlpatterns)
