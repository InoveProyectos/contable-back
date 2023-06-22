from rest_framework.views import APIView
from django.http import JsonResponse
from ..models import *
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
from datetime import datetime
import pytz
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
            total_entrada  += float(entrada[i]['monto'])
    
    except Exception as e:
        print(type(e).__name__)

    
    return total_entrada


def insert(entrada,fecha_registro,asiento, ingreso):
    """ Recibe  como entrada(debe o haber), fecha de registro y el objeto asiento
        informa con Http si fue creado 
    """
    try:
        for i in range(len(entrada)):
            cuenta = Cuenta.objects.filter(id=int(entrada[i]["cuenta_id"])).first()

            if cuenta.id:                 
                # Verificación de la fecha efectiva, que no sea None ni vacía.
                if entrada[i].get("fecha_efectiva")==None or entrada[i].get("fecha_efectiva")=="":
                    fecha_efectiva = fecha_registro
                else:
                    fecha_efectiva = entrada[i].get("fecha_efectiva")
                
                # Si el debe trae una cantidad
                monto = float(entrada[i].get("monto"))
                ingreso_debe = None
                ingreso_haber = None

                if monto != None and ingreso == "debe":
                    ingreso_debe = monto
                    ingreso_haber = 0

                elif monto != None and ingreso == "haber":
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
                                    observaciones = str(entrada[i].get("observaciones",'')),    
                                )
                registro.save()
                
            else: 
                print("El id ingresado no existe")
                return JsonResponse({}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    except Exception as e:
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
        Ejemplo de esquema de entrada:
        {"fecha_registro":"19/06/2023",
        "debe":[{"cuenta_id": 2, "concepto": "transferecia pago curso PI cuota 1", "numero_operacion": "cuota1", "monto": 500.50, "fecha_efectiva": ""}, {"cuenta_id": 2, "concepto": "Transferecia pago curso PI cuota 2", "numero_operacion": "cuota1","monto": 100,"fecha_efectiva": ""}],
        "haber":[{"cuenta_id": 5,"concepto": "Ingreso en banco","numero_operacion": "BBVA45068","monto": 500.50,"fecha_efectiva": ""},
        {"cuenta_id": 5,"concepto": "Ingreso en banco","numero_operacion": "BBVA45068","monto": 100,"fecha_efectiva": ""}]
        }      
    """
    
    parser_classes = (JSONParser,)
    
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
                if resultado == 0 and int(debe[0]["cuenta_id"]) != None and int(haber[0]["cuenta_id"]) != None:
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
                    
           
        except Exception as error:
            # Si aparece alguna excepción, devolvemos un mensaje de error
            return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST, safe=False, template_name=None, content_type=None)
    