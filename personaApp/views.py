from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import PersonaSerializer
from .models import  PersonaModel


class PersonaAPI(GenericAPIView):
    serializer_class = PersonaSerializer
    def post(self, request):
        persona_data = {}
        try:

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("STORED", status=status.HTTP_200_OK)

            # serializer = PersonaSerializer(data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response("STORED", status=status.HTTP_200_OK)
            # else:
            #     return Response(serializer.errors, status=status.HTTP_200_OK)

        except KeyError as e:
            return Response(str(e), status=status.HTTP_200_OK)
    
        
        
@api_view(['GET'])
def get(request):
    try:
        serializer = PersonaModel.objects.all()
        
        persona_serializer = PersonaSerializer(serializer,many=True) 
        
        return Response({'status':"GET ALL DATA","data":persona_serializer.data})
 
    except KeyError as e:
            return Response(str(e), status=status.HTTP_200_OK)    

        
        
        
@api_view(['GET'])
def get_data(request,pk):
    try:
        serializer = PersonaModel.objects.get(id=pk)
        
        persona_serializer = PersonaSerializer(serializer,many=False) 
        
        return Response({'status':"GET DATA","data":persona_serializer.data})
 
    except KeyError as e:
            return Response(str(e), status=status.HTTP_200_OK)  
    
            

