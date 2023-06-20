from rest_framework.views import APIView
from django.http import JsonResponse
from ..models import *
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
from datetime import datetime
import pytz



def sumatoria(entrada):
    """
    Entrada: lista de diccionarios
    Retorna la sumatoria del debe o haber que se 
    recibe por parámetro(entrada)
    """

    total_entrada = 0
    
    try:
        for i in range(len(entrada)):
            total_entrada  += float(entrada[i]['monto'])
    
    except Exception as e:
        print(type(e).__name__)

    
    return total_entrada


def insert(entrada,fecha_registro,asiento):
    """ Recibe  como entrada(debe o haber), fecha de registro y el objeto asiento
        informa con Http si fue creado 
    """
    try:
        for i in range(len(entrada)):
            Registro.objects.create(
                                cuenta = int(entrada[i]["cuenta_id"]),
                                asiento = asiento.id,
                                numero_operacion = entrada[i].get("numero_operacion"),
                                concepto = entrada[i]["concepto"],
                                #tipo_comprobante = entrada[i][""],
                                debe = float(entrada[i].get("debe",0)),
                                haber = float(entrada[i].get("haber",0)),
                                fecha_registro = fecha_registro,
                                fecha_efectiva = entrada[i].get("fecha_efectiva",fecha_registro),
                                #comprobante = entrada[i][""],
                                observaciones = str(entrada[i].get("observaciones",'')),    
                            )
        
        return JsonResponse({}, status=status.HTTP_200_OK)

            
    except Exception as e:
        #print(type(e).__name__)
        return JsonResponse(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RegistroAsientoAPIView(APIView):
    """ 
        Vista de API personalizada para recibir peticiones de tipo POST.
        NOTE: no puede generar un origen sin destino, ni lo contrario.
        debe- haber = 0, si se cumple se hace un registro sino informar el error  
        Bucle que reste total debe y total haber.

        Ingresar monto en Registro
        debe: destino del dinero
        haber: origen del dinero
        Esquema de entrada:
        {"fecha_registro":"19/06/2023",
        "debe":[{"cuenta_id": 2, "concepto": "transferecia pago curso PI cuota 1", "numero_operacion": "cuota1", "monto": 500.50, "fecha_efectiva": ""}, {"cuenta_id": 2, "concepto": "Transferecia pago curso PI cuota 2", "numero_operacion": "cuota1","monto": 100,"fecha_efectiva": ""}],
        "haber":[{"cuenta_id": 5,"concepto": "Ingreso en banco","numero_operacion": "BBVA45068","monto": 500.50,"fecha_efectiva": ""},
        {"cuenta_id": 5,"concepto": "Ingreso en banco","numero_operacion": "BBVA45068","monto": 100,"fecha_efectiva": ""}]
        }      
    """
    
    parser_classes = (JSONParser,)
    
    def post(self, request):
        user_data = {}
        try:
            # Obtenemos los datos del request:
            # fecha_registro = request.data['fecha_registro']
            fecha_registro= json.dumps(request.data["fecha_registro"])
            debe= json.dumps(request.data["debe"])  # Transforma a string
            haber= json.dumps(request.data["haber"])
            debe=json.loads(debe)                   # Transforma a dict
            haber=json.loads(haber)   
            fecha_registro = json.loads(fecha_registro).split("/")              

            if len(debe) != 0 and len(haber)!= 0:
                              
                total_debe = sumatoria(debe)
                total_haber = sumatoria(haber)       
                
                resultado = total_debe - total_haber
                if resultado == 0 and int(debe[0]["cuenta_id"]) != None and int(haber[0]["cuenta_id"]) != True:
                    # 1)Insertar un nuevo asiento (crear un nuevo, y quedarnos con 
                    # el objeto para usar su ID)
                    fecha_registro = datetime(day=int(fecha_registro[0]), month=int(fecha_registro[1]),year=int(fecha_registro[2]),tzinfo=pytz.UTC)
                                    
                    asiento = Asiento.objects.create(
                        fecha_registro = fecha_registro,
                    )
                    
                    insert(debe,fecha_registro,asiento)
                    insert(haber,fecha_registro,asiento)
                    
                    return JsonResponse(data={}, status=status.HTTP_200_OK)                   
                    
            else:
                user_data['response'] = "Error la resta del total de debe y haber no es igual a cero."
                return JsonResponse(user_data, status=status.HTTP_400_BAD_REQUEST,safe=False, template_name=None, content_type=None)

        
        except Exception as error:
            # Si aparece alguna excepción, devolvemos un mensaje de error
            return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST, safe=False, template_name=None, content_type=None)
    
    

    