from django.urls import path, include
from app.views.AuthView import login_view, logout_view

urlpatterns = [
    path("login/", login_view, name='login'),
    path("logout", logout_view, name='logout'),
    ]