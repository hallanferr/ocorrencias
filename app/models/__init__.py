#from .Protec import Protec

from django.db import models
from django.contrib.auth.models import User

CARACTERISTICA_LOCAL_CHOICES = (
    ("AGROPECUARIO", "Agropecuário"),
    ("COMERCIAL", "Comercial"),
    ("DE ENSINO", "De ensino")
    )
    

MEIO_UTILIZADO_CHOICES = (
    ("CICOM", "Cicom"),
    ("LINHA DIRETA", "Linha direta"),
    ("OUTRO", "Outro")
)

SITUACAO_CHOICES = (
    ("COM INTERVENCAO", "Com intervenção"),
    ("SI ENGANO", "S/I Engano"),
    ("SI TROTE", "S/I Trote"),
    ("SI SOLUCIONADO", "S/I Solucionado")
)

TIPO_DE_UTILIZACAO_CHOICES = (
    ("PRIVADA", "Privada"),
    ("PUBLICA", "Pública"),
    ("MISTA", "Mista")
)

POSTO_PREENCHEDOR_CHOICE = (
    ("SD BM", "Sd BM"),
    ("AL CB BM", "Al Cb BM"),
    ("CB BM", "Cb BM"),
    ("AL SGT BM", "Al Sgt BM"),
    ("SGT BM", "Sgt BM"),
    ("SUB TEN BM", "Subten BM"),
    ("AL OF BM", "Al Of BM"),
    ("ASP BM", "Asp BM"),
    ("TEN BM", "Ten BM"),
    ("CAP BM", "Cap BM"),
    ("MAJ BM", "Maj BM"),
    ("TC BM", "Tc BM"),
    ("CEL BM", "Cel BM")
)

ESTADOS_CHOICE = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espirito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
)

SISTEMA_PROTEC_CHOICES = (
    ("EXTINTOR", "Extintor"),
    ("SAIDA EMERGENCIA", "Saída de emergência"),
    ("ILUMINACAO", "Iluminação de emergência")
)

SIM_NAO_CHOICES = (
    ("SIM", "Sim"),
    ("NAO", "Não")
)
