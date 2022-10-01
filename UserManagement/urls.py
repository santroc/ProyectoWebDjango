from django.urls import path
from .views import *

#Para vista estándar de logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login_request, name = 'Login'),
    path('signup', register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name = 'Logout'),
    path('profile/', profile, name = 'profile'),
    path('profile/editProfile', editProfile, name = 'editProfile'),
    path('profile/changePass', change_pass, name = 'changePass'),
    path('profile/changePass', change_pass, name = 'changePass'),
    path('profile/changeAvatar', agregarAvatar, name ='changeAvatar')
]