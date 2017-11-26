from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView,ListCreateAPIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from user.models import Usuario
from user.serializers import UserSerializer#,UserLoginSerializer#, TokenSerializer

class UserCreateView(APIView):
    serializer_class = UserSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes= (AllowAny,) #(IsAuthenticated,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print request.user
        # print serializer
        print '****************************************************************************************************'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class UserCreateView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


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
