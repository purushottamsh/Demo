from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Client,CustomUser
from .serializers import ClientSerializer,ProjectInfoSerializer
from rest_framework import viewsets
from dj_rest_auth.views import LoginView
from .serializers import TokenSerializer
from django.contrib.auth import get_user_model


User=get_user_model()
class ClientListCreateAPIView(ListCreateAPIView):
    """ User Create View  """

    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):

        queryset = Client.objects.select_related('created_by')
        return queryset

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        elif self.request.user.is_authenticated:
            return Client.objects.filter(id=self.request.user.id)
        else:
            return Client.objects.none()


class ClientRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """ User RetrieveUpdate View  """

    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return ClientSerializer
        return self.serializer_class


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        elif self.request.user.is_authenticated:
            return Client.objects.filter(id=self.request.user.id)
        else:
            return Client.objects.none()


class UserViewSet(viewsets.ModelViewSet):
    """ User Create View  """

    queryset = CustomUser.objects.all ()
    serializer_class = ProjectInfoSerializer


    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomUser.objects.all ()
        elif self.request.user.is_authenticated:
            return CustomUser.objects.filter (id=self.request.user.id)
        else:
            return CustomUser.objects.none()

class CustomLoginAPI(LoginView):
    """ Custom Login API """
    def get_response(self):
        serializer_class = TokenSerializer
        serializer = serializer_class (instance=self.token)
        return Response(serializer.data ,status=status.HTTP_200_OK

