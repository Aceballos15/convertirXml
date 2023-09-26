from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import xmltodict
import json

class PrincipalView(APIView): 

    def post(self, request):
        xml_texto = request.data["xmlDocument"]

        xmlProcesado = self.limpiar_xml(xml_texto)
        json_convertido = self.convertDocument(xmlProcesado)
        return Response(json_convertido)
    


    def convertDocument(self, xmlDocument): 
        json_data = json.dumps(xmltodict.parse(xmlDocument), indent=4)
        return json_data



    def limpiar_xml(self, xmlDocument):
        # Elimina caracteres no imprimibles al principio del texto
        xml_texto = xmlDocument.lstrip('\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f ')
        return xml_texto

    