from rest_framework import generics, status
from rest_framework.response import Response


class AuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Hello'}, status=status.HTTP_200_OK)
