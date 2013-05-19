"""
URLconf for registration and activation, using django-registration's
default backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.default.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""


from django.conf.urls.defaults import *

from registration.views import activate
from registration.views import register

def template_view(template_name):
    try:
        from django.views.generic.simple import direct_to_template
        def curried_template_view(request, extra_context=None, mimetype=None, **kwargs):
            return direct_to_template(request, template_name, extra_context,
                mimetype, **kwargs)
        return curried_template_view
    except ImportError:
        from django.views.generic import TemplateView
        return TemplateView.as_view(template_name=template_name)

urlpatterns = patterns('',
                       url(r'^activate/complete/$',
                           template_view('registration/activation_complete.html'),
                           name='registration_activation_complete'),
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^activate/(?P<activation_key>\w+)/$',
                           activate,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_activate'),
                       url(r'^register/$',
                           register,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_register'),
                       url(r'^register/complete/$',
                           template_view('registration/registration_complete.html'),
                           name='registration_complete'),
                       url(r'^register/closed/$',
                           template_view('registration/registration_closed.html'),
                           name='registration_disallowed'),
                       (r'', include('registration.auth_urls')),
                       )
