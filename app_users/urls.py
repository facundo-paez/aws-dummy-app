from django.urls import path
from .views import UserListCreateView


app_name = 'app-users'
urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users'),
]
