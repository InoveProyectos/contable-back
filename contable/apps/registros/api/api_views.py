from rest_framework.views import APIView
from django.http import JsonResponse
from ..models import *
from rest_framework.parsers import JSONParser
from rest_framework import status


class RegistroAsientoAPIView(APIView):
    """ 
        Vista de API personalizada para recibir peticiones de tipo POST.
        Esquema de entrada:
        {"username":"root", "password":"12345"}


        Ingresar dinero en Registro
        debe: destino del dinero
        haber: origen del dinero
        
        NOTE: no puede generar un origen sin destino, ni lo contrario
        
        debe- haber = 0, si se cumple se hace un registro sino informar el error
            
            
        Bucle que reste total debe y total haber 
        
    """
    
    parser_classes = (JSONParser,)
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user_data = {}
        try:
            pass
        
        except Exception as error:
            # Si aparece alguna excepción, devolvemos un mensaje de error
            user_data['response'] = 'Error'
            #user_data['error_message'] = error
            return JsonResponse(user_data, status=status.HTTP_400_BAD_REQUEST)
    