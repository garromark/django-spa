from django.conf.urls.defaults import patterns, include, url

urlpatterns = \
    patterns('apps.index.views',
             url(r'^$', 'index'),
)
