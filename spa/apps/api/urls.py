from django.conf.urls.defaults import patterns, include, url
import spa.apps.user.urls
import spa.apps.s3.urls

urlpatterns = \
    patterns('spa.apps.api.views',
             url(r'^$', 'api_root'),
)

urlpatterns += \
    patterns('',
             url(r'^', include(spa.apps.user.urls)),
             url(r'^', include(spa.apps.s3.urls))
)
