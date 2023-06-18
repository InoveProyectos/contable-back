from rest_framework.views import APIView
from django.http import JsonResponse


class RegistroAsientoAPIView(APIView):
    """ Ingresar dinero en Registro
        debe: destino del dinero
        haber: origen del dinero"""