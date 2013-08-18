from django.conf.urls.defaults import patterns, include, url

urlpatterns = \
    patterns('spa.apps.index.views',
             url(r'^$', 'index'),
)
