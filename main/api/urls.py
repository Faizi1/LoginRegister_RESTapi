from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('getuser/',views.UserRegister.as_view()),
    path('register/',views.UserRegister.as_view()),
    path('login/',obtain_auth_token,name="login"),
]