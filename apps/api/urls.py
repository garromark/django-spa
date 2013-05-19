from django.conf.urls.defaults import patterns, include, url
import apps.user.urls
import apps.s3.urls

urlpatterns = \
    patterns('apps.api.views',
             url(r'^$', 'api_root'),
)

urlpatterns += \
    patterns('',
             url(r'^', include(apps.user.urls)),
             url(r'^', include(apps.s3.urls))
)
