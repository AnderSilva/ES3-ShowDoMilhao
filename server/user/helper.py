from user.serializers import UserStatusSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import BasePermission

def response_User_jwt_payload_handler(token, user=None, request=None):
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	print '****************************************************************'
	print dir(user)
	print '****************************************************************'
	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)
	data = {
		'token': token,
		'user': UserStatusSerializer(user).data
	}
	return data

class IsAdmin(BasePermission):
	def has_permission(self, request, view):
		return request.user and (request.user.is_admin==True)
