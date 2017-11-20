from rest_framework.generics import RetrieveAPIView,ListCreateAPIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework_jwt.views import obtain_jwt_token
from user.models import Usuario


# from users.serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer
from user.serializers import UserSerializer,UserLoginSerializer, TokenSerializer

class UserCreateView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class UserLoginView(CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    # queryset = Usuario.objects.all()
    # serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        # print serializer.data #['senha']
        # print serializer['data']
        if serializer.is_valid():
            # print serializer
            # login = serializer['login']
            # token = serializer['csrfmiddlewaretoken']
            # user_db = Usuario.objects.get(pk=xlogin)
            pass
        # token, _ = Token.objects.get_or_create(user=login)
        return Response(data={'sucesso!'},status=status.HTTP_200_OK)


# class UserLoginAPIView(GenericAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.user
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response(
#                 data=TokenSerializer(token).data,
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


# class UserLogoutAPIView(APIView):

#     def post(self, request, *args, **kwargs):
#         Token.objects.filter(user=request.user).delete()
#         return Response(status=status.HTTP_200_OK)
