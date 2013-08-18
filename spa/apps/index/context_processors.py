# source: https://gist.github.com/mmalone/156638

from django.views import debug

view_settings = dict(((k.lower(), v) for (k, v) in
                        debug.get_safe_settings().iteritems()))

def settings(request):
    """
    Provides a 'settings' context variable that is a subset of the
    Django settings module (the 'safe' settings).
    """
    return {
        'settings': view_settings,
    }
