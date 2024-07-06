from django.urls import path
from .views import register, profile, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
urlpatterns += [
    path('users/', include('users.urls')),
]
