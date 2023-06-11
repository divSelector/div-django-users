from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import UserView

urlpatterns = [
    path('',  login_required(UserView.as_view()), name='profile'),
]