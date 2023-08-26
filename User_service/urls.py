from django.urls import path, include
from .import views


urlpatterns = [
    path("users/", views.UserList.as_view(), name="users_list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user_details"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
] 