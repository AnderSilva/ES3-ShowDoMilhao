from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
#from user.views import UserCreateView, UserDetailView #UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView
from user.views import UserCreateView,UserListView,UserGetView

urlpatterns = [
    url(r'^/create$'         , UserCreateView.as_view()),
    url(r'^/token/get$'      , obtain_jwt_token),
    url(r'^/token/refresh$'  , refresh_jwt_token),
    url(r'^/list$'           , UserListView.as_view()),
    url(r'^/(?P<pk>[0-9]+)$' , UserGetView.as_view()),
    

    
    # url(r'^/login/verify$', verify_jwt_token),



    #url(r'^/$'			, UserCreateView.as_view()		, name="user_create"),
    ## url(r'^/login$'		, UserLoginView.as_view()		, name="user_login"),
    #url(r'^/(?P<pk>[0-9]+)$', UserDetailView.as_view()	, name='user_detail'),
    ## url(r'^/$'		, UserRegistrationAPIView.as_view() , name="user_list"),
    ## url(r'^logout/$'		, UserLogoutAPIView.as_view()		, name="logout"),
]
