from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView

urlpatterns = [
    path('profile/',  login_required(UserView.as_view()), name='profile'),
]