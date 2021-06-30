# from django.shortcuts import render, render_to_response
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import userprofile, assignTaskFiles, loginprofile, objectLevel, SceneLevel
from .serializers import UpdateSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.shortcuts import render
# Create your views here.
class SnippetList(APIView):   
    def post(self, request):
        print (request.data)
        obj = loginprofile()  # gets new object
      
        obj.firstName = request.data['firstName']
        obj.role = request.data['role']
        obj.password = request.data['password']
        obj.save()
        return Response('sucesssfully')

class ObjectLevel(APIView):   
    def post(self, request):
        print (request.data)
        obj = objectLevel() 
        obj.trackId = request.data['trackId']
        obj.objectClass = request.data['objectClass']
        obj.pose = request.data['pose']
        obj.occlusion = request.data['occlusion']
        obj.lane_change = request.data['lane_change']
        obj.breakLight = request.data['breakLight']
        obj.save()
        return Response('sucesssfully')

class SceneLevelQuery(APIView):   
    def post(self, request):
        print (request.data)
        obj = SceneLevel() 
        obj.Light_Condition = request.data['Light_Condition']
        obj.Road_Type = request.data['Road_Type']
        obj.Road_works = request.data['Road_works']
        obj.Tunnel = request.data['Tunnel']
        obj.Weather = request.data['Weather']
        obj.Street_Condition = request.data['Street_Condition']
        obj.save()
        return Response('sucesssfully')


class GetObjectLevel(APIView):
    def get(self, request):
            values1 = objectLevel.objects.all().values()
            print(values1)
            return Response(values1)

class GetSceneLevel(APIView):
    def get(self, request):    
            values1 = SceneLevel.objects.all().values()
            print(values1)
            return Response(values1)

class Login(APIView):
    def post(self, request):
        cred=request.data
        name=request.data['firstName']
        password=request.data['password']
        #role=request.data['role']
        print("cred",cred)
        check=loginprofile.objects.filter(firstName=name,password=password).values()
        if check:
            return Response("Login Succesfull")
        else:
            return Response("Invalid Credentials")



class TaskFiles(APIView):
     def post(self, request):
        print (request.data)
        obj = assignTaskFiles()  # gets new object
        obj.File_Name = request.data['File_Name']
        obj.Task_level = request.data['Task_level']
        obj.Priority = request.data['Priority']
        obj.Created_Date = request.data['Created_Date']
        obj.status = request.data['status']
        obj.Action = request.data['Action']
        obj.save()
        return Response('sucesssfully')

        

class GetTaskFilesList(APIView):
    def get(self, request):
            print (request.data)
            entry = assignTaskFiles.objects.all().values()
            return Response(entry)

class Getuser(APIView):
    def get(self, request):
        print (request.data)
        entry = loginprofile.objects.all().values()
        print("entry",entry)
        return Response(entry)

class UserRoles(APIView):
     def get(self, request):
         list = loginprofile.objects.values("role")
         if(loginprofile.objects.values("role") == "maker"):
             return Response(list)



class Deleterecords(APIView):
    def delete(self, request):
            print (request.data)
           # firstName = request.data['firstName']
            loginprofile.objects.all().delete()
            print (request.data)
            return Response("deleted sucesfuly")


class Updateuser(APIView):
    def put(self, request):
        obj = loginprofile()
        id = request.data['id']
        loginprofile.objects.filter(id=id).update(firstName=request.data['firstName'],
        password=request.data['password'])
        loginprofile.objects.filter(id=id).update()
        obj.save()
        details = userprofile.objects.filter(id=id)
        serializer = UpdateSerializer(details,id)    
        return Response("Updated")
        print("*********",serializer.errors)