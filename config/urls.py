from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
import apps.registration.urls
import apps.index.urls
import apps.api.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include(apps.registration.urls)),
                       url(r'^', include(apps.index.urls)),
                       url(r'^api/', include(apps.api.urls)),
                       url(r'^api-auth/$', include('rest_framework.urls',
                                                   namespace='rest_framework'))
                       )

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
