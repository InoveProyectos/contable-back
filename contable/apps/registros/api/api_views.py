import json
from datetime import datetime

from django.http import JsonResponse
from django.db import transaction

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status

from ..models import *
from ..api.serializers import *



def sumatoria(entrada):
    """
    Entrada: lista de diccionarios
    Retorna la sumatoria del debe o haber que se 
    recibe por parámetro(entrada)
    """

    total_entrada = 0
    
    try:
        for i in range(len(entrada)):
            total_entrada  += entrada[i]['monto']
    
    except Exception as e:
        print(type(e).__name__)

    
    return total_entrada


def insert(entrada,fecha_registro,asiento, ingreso):
    """ Recibe  como entrada(debe o haber), fecha de registro y el objeto asiento
        informa con Http si fue creado 
    """

    for i in range(len(entrada)):
        cuenta = Cuenta.objects.get(id=entrada[i]["cuenta_id"])
                
        # Verificación de la fecha efectiva, que no sea None ni vacía.
        if entrada[i].get("fecha_efectiva") is None or entrada[i].get("fecha_efectiva") == "":
            fecha_efectiva = fecha_registro
        else:
            fecha_efectiva = entrada[i].get("fecha_efectiva")

        # Si el debe trae una cantidad
        monto = entrada[i]["monto"]
        ingreso_debe = None
        ingreso_haber = None

        if monto is not None and ingreso == "debe":
            ingreso_debe = monto
            ingreso_haber = 0

        elif monto is not None and ingreso == "haber":
            ingreso_debe = 0
            ingreso_haber = monto
            
        registro = Registro.objects.create(
                            cuenta = cuenta,
                            asiento = asiento,
                            numero_operacion = entrada[i].get("numero_operacion"),
                            concepto = entrada[i]["concepto"],
                            tipo_comprobante = entrada[i].get("tipo_comprobante") ,
                            debe = ingreso_debe,
                            haber = ingreso_haber,
                            fecha_registro = fecha_registro,
                            fecha_efectiva = fecha_efectiva,
                            comprobante = entrada[i].get("comprobante"),
                            observaciones = entrada[i].get("observaciones",''),
                        )
        registro.save()



class RegistroAsientoAPIView(APIView):
    """ 
        Vista de API personalizada para recibir peticiones de tipo POST.
        Ejemplo de esquema de entrada:
        {
            "fecha_registro":"19/06/2023",
            "debe":[
                {
                    "cuenta_id": 1,
                    "concepto": "Transferecia pago curso PI cuota 1",
                    "numero_operacion": "cuota1",
                    "monto": 500.50,
                },
                ],
            "haber":[
                {
                    "cuenta_id": 2,
                    "concepto": "Ingreso en banco",
                    "numero_operacion": "BBVA45068",
                    "monto": 500.50,
                },
            ]
        }
        NOTE: no puede generar un origen sin destino, ni lo contrario.
        debe- haber = 0, si se cumple se hace un registro sino informar el error  
        Bucle que reste total debe y total haber.

        Ingresar monto en Registro
        debe: destino del dinero
        haber: origen del dinero   
    """
    
    parser_classes = (JSONParser,)
    
    @transaction.atomic
    def post(self, request):
        
        try:
            # Obtenemos los datos del request:
            debe = request.data["debe"]
            haber = request.data["haber"]
            fecha_registro = request.data["fecha_registro"]

            if len(debe) != 0 and len(haber)!= 0:
                total_debe = sumatoria(debe)
                total_haber = sumatoria(haber)       
                
                resultado = total_debe - total_haber
                if resultado == 0:
                    # 1)Insertar un nuevo asiento (crear un nuevo, y quedarnos con 
                    # el objeto para usar su ID)
                    # Convierte la fecha str en un objeto datetime
                    fecha_registro = datetime.strptime(fecha_registro, "%d/%m/%Y")
                    print("fecha_registro",fecha_registro)
                    
                    # Crea el asiento
                    asiento_create = Asiento.objects.create(
                        fecha_registro = fecha_registro,
                        )
                    asiento_create.save()

                    asiento = Asiento.objects.filter(fecha_registro = fecha_registro).first()
                    insert(debe,fecha_registro,asiento, "debe")
                    insert(haber,fecha_registro,asiento, "haber")
                    
                                        
                    return JsonResponse(data={}, status=status.HTTP_200_OK)
                    
                else:
                    return JsonResponse(data={"error": "error en balance de registros"}, status=status.HTTP_400_BAD_REQUEST)
           
        except Exception as error:
            # Si aparece alguna excepción
            # Anulamos los campos de la base de datos (rollback)
            transaction.set_rollback(True)
            # Devolvemos un mensaje de error
            return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
    