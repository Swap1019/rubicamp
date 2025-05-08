from django.urls import path
from .views import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    HomeView,
    AboutView,
    WebsiteCreateView,
    UserInfoCreateView,
    RedirectView,
    UserGeneratedWebsiteView,
    UserCongratulations,
)

app_name = "rubikamp"

urlpatterns = [
    path('',HomeView.as_view(),name='Home' ),
    path('about/',AboutView.as_view(),name='about'),
    path('createyourwebsite/',WebsiteCreateView.as_view(),name='user-website-create' ),
    path('createyourwebsite/created',UserCongratulations.as_view(),name='user-website-congratulations' ),
    path('user/redirect/', RedirectView.as_view(), name='user-redirect'),
    path('user/redirect/create/', UserInfoCreateView.as_view(), name='user-info-create'),  
    path('user/yourwebsite/', UserGeneratedWebsiteView.as_view(), name='user-website-generated'),  
    path('register/',RegisterView.as_view(),name='user-register' ),
    path('login/',UserLoginView.as_view(),name='user-login' ),
    path('logout/',UserLogoutView.as_view(),name='user-logout' ),

]