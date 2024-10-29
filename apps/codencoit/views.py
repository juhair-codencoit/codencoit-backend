from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *


# ====== Team Member API =========#

class TeamMemberList(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def get(self , request):
        query = TeamMember.objects.all()
        serializer = TeamMemberSerializers(query , context= {'request':request}, many=True)
        if serializer :
            return Response(serializer.data, status=status.HTTP_200_OK,)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self , request):
        serializer = TeamMemberSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST) 
    
    
class TeamMemberDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request , pk):
        member = get_object_or_404(TeamMember, id=pk )
        serializer = TeamMemberSerializers(member, context= {'request':request})
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self, request , pk):
        member = get_object_or_404(TeamMember, id=pk )
        serializer = TeamMemberSerializers(instance = member , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = get_object_or_404(TeamMember, id=pk )
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ====== Industry API =========#

class IndustryList(APIView):

    def get(self,request):
        query = Industry.objects.all()
        serializer = IndustrySerializers(query,context = {'request':request} ,many=True)
        if serializer :
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        serializer = IndustrySerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

class IndustryDetail(APIView):

    def get(self, request, pk):
        industry = get_object_or_404(Industry, id = pk)
        serializer = IndustrySerializers(industry , context= {'request':request})
        return Response(serializer.data , status= status.HTTP_200_OK)
    
    def put(self, request, pk):
        industry = get_object_or_404(Industry, id = pk)
        serializer = IndustrySerializers(instance = industry , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        industry = get_object_or_404(Industry, id=pk )
        industry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ====== Project API =========#

class ProjectList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        project = Projects.objects.all()
        serializer = ProjectSerializers(project,context= {'request':request}, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):

        serializer = ProjectSerializers(data = request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):

    def get(self, request, pk):
        project = get_object_or_404(Projects, id = pk)
        serializer = ProjectSerializers(project, context={'request':request})
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self,request, pk):
        project = get_object_or_404(Projects, id=pk)
        serializer = ProjectSerializers(instance = project , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = get_object_or_404(Projects, id=pk )
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)