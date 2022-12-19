import json
from django.shortcuts import render

from .models import JsonModel
from loginApp.models import CustomUsersV2
from .serializers import JsonFileSerializer
from .authentication import ExpiringTokenAuthentication

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

class JsonListView(APIView):
    # authentication_classes = [ExpiringTokenAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # parser_classes = [JSONParser]

    def get(self, request, format=None): 

            jsondata = JsonModel.objects.all()
            serializer = JsonFileSerializer(jsondata,many=True)
            data = serializer.data
            return Response(data)


    def post(self,request,format=None):
        
        save_state = {}

        serializer = JsonFileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user= request.user)
            save_state["state"] = "FILE_SAVED"

        else:
            save_state["state"] = "FILE_NOT_SAVED"
            save_state["error"] = serializer.errors

        return Response(save_state, status=status.HTTP_200_OK)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class JsonDetailView(APIView):
    # authentication_classes = [ExpiringTokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get_object(self, pk):
        try:
            return JsonModel.objects.get(pk=pk)
        except:
            return "FILE_NOT_FOUND"

    def get(self, request,pk, format=None): 

            image_data = {}

            jsondata = self.get_object(pk)

            if jsondata == "FILE_NOT_FOUND":
                image_data["state"] = "FILE_NOT_FOUND"
            
            else:
                serializer = JsonFileSerializer(jsondata)
                image_data["state"] = "FILE_FOUND"
                image_data["data"] = serializer.data

            return Response(image_data, status=status.HTTP_200_OK)



class SaveAllAPI(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        
        save_state = {}
        data = request.data["data"]

        try:
            for i in data:
                serializer = JsonFileSerializer(data=i)
                if serializer.is_valid():
                    serializer.save()
                else:
                    continue
            save_state["state"] = "FILES_SAVED"
            return Response(save_state, status=status.HTTP_200_OK)

        except:
            save_state["state"] = "FILES_NOT_SAVED"
            return Response(save_state, status=status.HTTP_200_OK)



