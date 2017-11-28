from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from user.helper import IsAdmin,IsAdmin_Authenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView,RetrieveAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer


from user.serializers import UserSerializer, UserUpdateSerializer,UserStatusSerializer
from user.models import Usuario

class UserListView(ListAPIView): #
	"""
	Lista os usuarios do Sistema (AdminOnly)
	"""
	permission_classes= (IsAdmin,)
	queryset = Usuario.objects.all()
	serializer_class = UserSerializer

class UserCreateView(CreateAPIView): #Create
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

class UserGetView(RetrieveUpdateAPIView): #/user/<pk>
	"""
	Visualizacao de usuarios  (Admin: visualiza qualquer usuario, outros:somente seu usuario)
	"""
	permission_classes= (IsAdmin_Authenticated,)
	queryset = Usuario.objects.all()
	serializer_class = UserSerializer

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT': #and self.update_serializer_class:
			serializer_class = UserUpdateSerializer        
		if self.request.method == 'PATCH':# and self.update_serializer_class:
			serializer_class = UserUpdateSerializer        
		return serializer_class

	def get(self, request, pk, format=None):
		serializer = self.serializer_class(data=request.data)

		user_request = Usuario.objects.get(id=request.user.id)
		print int(request.user.id) == int(pk)

		if not (request.user.is_admin or int(request.user.id) == int(pk)):
			return Response({'errors': 'Acesso nao autorizado.'},status=status.HTTP_401_UNAUTHORIZED)                    
		
		return Response(UserSerializer(user_request).data, status=status.HTTP_200_OK)

	def put(self, request, pk, format=None):
		serializer = self.serializer_class(data=request.data)

		user_request = Usuario.objects.get(id=request.user.id)
		print int(request.user.id)# == int(pk)

		if not (request.user.is_admin or int(request.user.id) == int(pk)):
			return Response({'errors': 'Acesso nao autorizado.'},status=status.HTTP_401_UNAUTHORIZED)                    
		
		if serializer.is_valid():        
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)


class UserView(RetrieveUpdateAPIView): #/user/
	"""
	Visualizacao do usuario authenticado
	"""
	permission_classes= (IsAdmin_Authenticated,)
	queryset = Usuario.objects.all()
	serializer_class = UserStatusSerializer

	# def get_serializer_class(self):
	# 	serializer_class = self.serializer_class

	# 	if self.request.method == 'PUT': #and self.update_serializer_class:
	# 		serializer_class = UserUpdateSerializer        
	# 	if self.request.method == 'PATCH':# and self.update_serializer_class:
	# 		serializer_class = UserUpdateSerializer        
	# 	return serializer_class

	def get(self, request, format=None):
		user_request = Usuario.objects.get(id=request.user.id)
		
		return Response(self.serializer_class(user_request).data, status=status.HTTP_200_OK)

	def put(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		# user_request = Usuario.objects.get(id=request.user.id)
		
		if serializer.is_valid():        
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

# class UserUpdateView(UpdateAPIView): #/user/update/<pk>
#     """
#     Alteracao de usuarios  (Admin: altera qualquer usuario, outros:somente seu usuario)
#     """
#     permission_classes= (IsAdmin_Authenticated,)
#     queryset = Usuario.objects.all()
#     serializer_class = UserUpdateSerializer

#     def put(self, request, pk, format=None):
#         serializer = self.serializer_class(data=request.data)

#         user_request = Usuario.objects.get(id=request.user.id)
#         print int(request.user.id) == int(pk)

#         if not (request.user.is_admin or int(request.user.id) == int(pk)):
#             return Response({'errors': 'Acesso nao autorizado.'},status=status.HTTP_401_UNAUTHORIZED)                    
		
#         if serializer.is_valid():        
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
		
#         return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)




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
