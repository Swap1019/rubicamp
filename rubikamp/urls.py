from django.urls import path
from .views import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    HomeView,
    AboutView,
    WebsiteCreateView,
)

app_name = "rubikamp"

urlpatterns = [
    path('',HomeView.as_view(),name='Home' ),
    path('about/',AboutView.as_view(),name='about'),
    path('createyourwebsite/',WebsiteCreateView.as_view(),name='user-website-create' ),
    path('register/',RegisterView.as_view(),name='user-register' ),
    path('login/',UserLoginView.as_view(),name='user-login' ),
    path('logout/',UserLogoutView.as_view(),name='user-logout' ),
]