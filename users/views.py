"""User views"""
from rest_framework import authentication, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserListCreateView(APIView):
    """_Listing all users. Requires token authentication.
    Only admins can access the view
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """Listing user full names"""
        users = [user.full_name for user in User.objects.all()]
        return Response(users)


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
