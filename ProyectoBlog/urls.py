from django.urls import path
from ProyectoBlog.views import *

#Para vista estándar de logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PostList.as_view(), name='Inicio'),
    path(r'^(?P<pk>\d+)$', PostDetail.as_view(), name='post_detail'),
    path(r'^borrar/(?P<pk>\d+)$', PostDelete.as_view(),name="post_delete"),
    path(r'^editar/(?P<pk>)$', PostUpdate.as_view(), name = "post_update"),
    path('deletePost/<post_id>', deletePost, name='post_delete_nv'),
    path('addPost', addPost, name='addPost'),
    path('searchPost', busquedaPost, name='busquedaPost'),
    path('search/', buscar),
    path('login', login_request, name = 'Login'),
    path('register', register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name = 'Logout'),
    path('profile/', profile, name = 'profile'),
    path('profile/editProfile', editProfile, name = 'editProfile'),
    path('profile/changePass', change_pass, name = 'changePass'),
    path('profile/changePass', change_pass, name = 'changePass'),
    path('profile/changeAvatar', agregarAvatar, name ='changeAvatar')
]