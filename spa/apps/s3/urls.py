from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from spa.apps.s3 import views

urlpatterns = \
    patterns('apps.s3.views',
             url(r'^s3/form', views.S3Form.as_view(), name='s3-form'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
