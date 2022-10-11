from django.shortcuts import render
from .serializers import TaskSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import Task
@api_view(['GET'])
def my_api_view(request):
    data = {
        'text': 'Hello, my team !'
    }

    return Response(data)

@api_view(['GET'])
def tasklist_view(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)
#
# @api_view(['GET'])
# def task_details_view(request):
#     tasks = Task.objects.all()
#     data_ = {}
#     for i in tasks:
#         data_[i.title] = i.completed
#     return Response(data_)

@api_view(['GET'])
def taskdetail_view(request, id):
    if Task.objects.get(id=id):
        serializer = TaskSerializers(Task.objects.get(id=id))
        return Response(serializer.data)

@api_view(['POST'])
def taskcreate_view(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({'Created': 'Object is created !'})


class TasksAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TaskSerializers(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

@api_view(['POST'])
def taskupdate_view(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete_view(request, id):
    task = Task.objects.get(id=id)
    if task:
        task.delete()
        return Response('Обьект удален.')

