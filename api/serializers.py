from .models import Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.save()
        return instance

# class TasksSerializers(serializers.Serializer):
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.completed = validated_data.get("completed", instance.completed)
#         instance.save()
#         return instance
