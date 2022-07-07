from rest_framework import permissions, authentication


class AuthPermMixin():
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
