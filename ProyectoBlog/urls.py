from django.urls import path
from ProyectoBlog.views import *

#Para vista estándar de logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PostList.as_view(), name='Inicio'),
    path('<pk>/', PostDetail.as_view(), name='post_detail'),
    path('borrar/<pk>', PostDelete.as_view(),name="post_delete"),
    path('editar/<pk>', PostUpdate.as_view(), name = "post_update"),
    path('editar_admin/<pk>', PostUpdateAdmin.as_view(), name = "post_update_admin"),
    path('deletePost/<post_id>', deletePost, name='post_delete_nv'),
    path('addPost', addPost, name='addPost'),
    path('searchPost', busquedaPost, name='busquedaPost'),
    path('search/', buscar),
    path('about', about_us),
    path('messages/inbox', show_inbox.as_view(), name = 'inbox'),
    path('messages/<int:pk>/', msg_detail.as_view(), name = 'message_detail'),
    path('messages/new/', create_msg.as_view(), name = 'new_msg'),
    path('messages/reply/<int:sender>', reply_msg.as_view(), name = 'reply_msg'),

    #path('test', is_User_Super)
    # path('login', login_request, name = 'Login'),
    # path('register', register, name = 'Register'),
    # path('logout', LogoutView.as_view(template_name='logout.html'), name = 'Logout'),
    # path('profile/', profile, name = 'profile'),
    # path('profile/editProfile', editProfile, name = 'editProfile'),
    # path('profile/changePass', change_pass, name = 'changePass'),
    # path('profile/changePass', change_pass, name = 'changePass'),
    # path('profile/changeAvatar', agregarAvatar, name ='changeAvatar')
]