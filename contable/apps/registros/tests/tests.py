from apps.registros.models import TipoEntidad
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TipoEntidadViewSetTestCase(APITestCase):

    # ---||| Parte N1 |||---
    def setUp(self):
        '''Crear un registro'''
        #________________________________________________________________________________________
        self.url = reverse('tipo_entidad_vs-list') # name del endpoint conseguido en el browser: http://127.0.0.1:8000/registros// 
        
        # ||| Parte 1||| Se crea el registro, a través de la variable tipo_entidad_new que guarda la creación del registro
        self.tipo_entidad_new = TipoEntidad.objects.create(
                        name="Juridica"
                        )
        #print('Create DB backend:', {'id':self.tipo_entidad_new.id, 'name':self.tipo_entidad_new.name})

        #_________________________________________________________________________________________
        # ||| Parte 2||| Se hace el post a través del self.cliente, necesita la url+data+formato
        response = self.client.post(self.url, 
        {
            'name':'Fisica'
        },
        format='json')
        #print('create post cliente:',response.json())

        #__________________________________________________________________________________________
        # Consultar todo para verificar que guardó
        # todo = TipoEntidad.objects.all()
        # print('todo:',todo)
       
        
        #print(response.json()['name']) ## Show the name save in the DB of client
        #print('ver_1:',response.status_code) ## Show the code of status of client
        #print('ver_2',status.HTTP_201_CREATED)  ## Show the code of status of back

        #__________________________________________________________________________________________
        # Verifica la igualdad entre ambos status si tanto el cliente como el back registraron los registros en la DB
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Ambos fueron creados con exito, por el cliente response.status_code y el backend status.HTTP_201_CREATED
        self.assertEqual(response.json()['name'], 'Fisica') # Compara si el name enviado por el cliente en el post es igual al indicado
        return super().setUp()
    

    def test_read(self):
        """ Lee los registros por id y todos"""

        # Se consulta por ID
        self.url = f'/registros/tipo_entidad_vs/{self.tipo_entidad_new.id}/'
        response_1 = self.client.get(self.url)
        #print(response_1.json())

        # Se consulta toda la información
        self.url = f'/registros/tipo_entidad_vs/'

        # ADD otro registro
        self.client.post(self.url, 
            {
                'name':'Fisica'
            },
            format='json')

        # Consulta todos los registros
        response_3 = self.client.get(self.url)
        #print('read_3',response_3.json())

        self.assertEqual(response_1.status_code, response_3.status_code)


    def test_put(self):
        """ Actualiza un registro"""

        # Url
        self.url = f'/registros/tipo_entidad_vs/{self.tipo_entidad_new.id}/'  ## Funciona       
      
        response_1 = self.client.put(self.url, data={'name':'Fisica_put'}) # url+data={}
        #print('Put',response_1.status_code)

        #Consultando el registro para compararlo con el put realizado
        response_2 = self.client.get(self.url)

        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_1.json(), response_2.json())
       

    def test_delete(self):
        '''Elimina un registro'''
        
        # Url
        self.url = f'/registros/tipo_entidad_vs/{self.tipo_entidad_new.id}/'  ## Funciona
        
        # Consulta por id usando la url
        #response_1 = self.client.get(self.url)
        #print('consulta_cliente:',response_1.json())
        
        response = self.client.delete(self.url)
        #print('Delete',response)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) # 204 sin contenido
        self.assertFalse(TipoEntidad.objects.filter(id=self.tipo_entidad_new.id).exists()) # Busca en la DB si está el registro por id y como no esta es False y lo verifica con el assertFalse
    

    
       
            
        
       
        

        
        


        
        

    
       
    