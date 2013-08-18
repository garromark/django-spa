from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    user = request.user
    return Response({
        'user-id': user.id,
        'user-username': user.username,
        'user-firstname': user.first_name,
        'user-lastname': user.last_name,
        'users': reverse('user-list', request=request, format=format),
        's3-form': reverse('s3-form', request=request, format=format),
        })
