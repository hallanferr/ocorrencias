from django.urls import path
from app.views.HomeView import home_view

urlpatterns = [
    path("", home_view, name='home_view')
]
