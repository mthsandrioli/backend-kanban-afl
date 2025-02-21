from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Projects, Tasks, Stages
from .serializer import ProjectSerializer, TaskSerializer, StageSerializer

@api_view(['GET'])
def get_projects(request):
    projects = Projects.objects.all()
    serializedData = ProjectSerializer(projects, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_project(request):
    data = request.data
    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def project_settings(request, id):
    try:
        project = Projects.objects.get(id=id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tasks(request):
    tasks = Tasks.objects.all()
    serializedData = TaskSerializer(tasks, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_task(request):
    data = request.data
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def task_settings(request, id):
    try:
        tasks = Tasks.objects.get(id=id)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = TaskSerializer(tasks, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_stages(request):
    stages = Stages.objects.all()
    serializedData = StageSerializer(stages, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_stage(request):
    data = request.data
    serializer = StageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def stage_settings(request, id):
    try:
        stages = Stages.objects.get(id=id)
    except Stages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        stages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = StageSerializer(stages, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
