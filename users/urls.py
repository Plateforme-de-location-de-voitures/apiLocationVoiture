from django.urls import path
from .views import *

urlpatterns = [
    path('roles', RoleListAPIView.as_view(), name='liste_roles'),
    path('role/<int:role_id>', RoleDetailAPIView.as_view(), name="detail_role"),
    path('role/create', CreateRoleAPIView.as_view(), name='role_create'),
    path('register', RegisterAPIView.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name='login'),
    path('user', GetUserAPIView.as_view(), name='user'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
]