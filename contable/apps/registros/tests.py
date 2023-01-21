from django.test import TestCase

#-----------------------
from rest_framework.test import APITestCase
#from django.contrib.auth.models import User
from .models import TipoEntidad
from apps.registros.api.serializers import TipoEntidadSerializer
from rest_framework import status
# ---
from .models import *
from django.urls import reverse
