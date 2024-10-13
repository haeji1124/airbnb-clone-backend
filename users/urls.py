from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.Users.as_view()),
    path("logout", views.LogOut.as_view()),
    path("login", views.LogIn.as_view()),
    path("token-login", obtain_auth_token),
    path("jwt-login", views.JWTLogIn.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
    path("password", views.ChangePassword.as_view()),
    path("me", views.Me.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
]
