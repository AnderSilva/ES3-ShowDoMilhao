from django.conf.urls import url
from user.views import UserCreateView, UserLoginView, UserDetailView #UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    # url(r'^/$'		, UserRegistrationAPIView.as_view() , name="user_list"),
    url(r'^/$'			, UserCreateView.as_view()		, name="user_create"),
    url(r'^/login$'		, UserLoginView.as_view()		, name="user_login"),
    url(r'^/(?P<pk>[0-9]+)$', UserDetailView.as_view()	, name='user_detail'),
    # url(r'^logout/$'		, UserLogoutAPIView.as_view()		, name="logout"),
]
