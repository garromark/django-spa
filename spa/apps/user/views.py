from django.contrib.auth.models import User
from rest_framework import generics
from spa.apps.user.serializers import UserSerializer
from spa.apps.api.permissions import IsSelf

class UserList(generics.ListCreateAPIView):
    """
    List all the users or create new one.
    Note that registration does NOT use this - it uses the
    views in the registration app.
    """
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        We restrict the listing of users to display only the
        currently logged in user.
        """
        user = self.request.user
        return User.objects.filter(pk=user.id)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve info about the user
    """
    model = User
    serializer_class = UserSerializer
    permission_classes = (IsSelf,)
