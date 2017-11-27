from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from user.helper import IsAdmin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer
from user.models import Usuario

class UserListView(ListAPIView):
    """
    Lista os usuarios do Sistema (AdminOnly)
    """
    permission_classes= (IsAdmin,)
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class UserCreateView(CreateAPIView):
    """
    Criacao de usuarios  (Any)
    """
    serializer_class = UserSerializer    
    permission_classes= (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class UserGetView(RetrieveUpdateAPIView):
    """
    Alteracao de usuarios  (Admin: altera qualquer usuario, outros:somente seu usuario)
    """
    permission_classes= (IsAuthenticated,)
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(data=request.data)
        print request
        # allowed = Usuario.objects.get(request.user.id)
        # print allowed
        print '*******************************************************'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



# class UserDetailView(RetrieveUpdateAPIView):
#     permission_classes= (IsAuthenticated,)
#     queryset = Usuario.objects.all()
#     serializer_class = UserSerializer


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
