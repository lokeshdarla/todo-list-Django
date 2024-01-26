# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_list(request):
    tasks = Task.objects.filter(author=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    task = Task.objects.filter(author=request.user, pk=pk).first()
    if task:
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    else:
        return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_update(request, pk):
    task = Task.objects.filter(pk=pk).first()

    if task:
        if task.author != request.user:
            return Response({"detail": "You do not have permission to update this task."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_delete(request, pk):
    task = Task.objects.filter(author=request.user, pk=pk).first()
    if task:
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
