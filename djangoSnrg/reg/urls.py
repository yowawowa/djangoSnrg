from django.urls import path
from reg.views import register

urlpatterns = [
    path('', register, name='Register'),
]
