from user.serializers import UserStatusSerializer

def response_User(token, user=None,request=None):
    return {
        'token': token,
        'user': UserStatusSerializer(user).data
}
