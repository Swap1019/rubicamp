from django.urls import path
from .views import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    HomeView,
)

app_name = "rubikamp"

urlpatterns = [
    path('home/',HomeView.as_view(),name='Home' ),
    path('register/',RegisterView.as_view(),name='user-register' ),
    path('login/',UserLoginView.as_view(),name='user-login' ),
    path('logout/',UserLogoutView.as_view(),name='user-logout' ),
]