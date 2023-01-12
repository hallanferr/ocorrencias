from django.urls import path
from app.views.OcorrenciaView import create_ocorrencia

urlpatterns = [
    path("new/", create_ocorrencia, name='create_ocorrencia')
    ]