from django.urls import path
from .views import user_login, user_logout

urlpatterns = [
    path('', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]
