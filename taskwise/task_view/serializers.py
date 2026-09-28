from rest_framework import serializers
from task_view.models import Task
class UserSeralizer(serializers.Serializer):

    id=serializers.CharField(read_only=True)

    username=serializers.CharField()

    email=serializers.EmailField()

    password=serializers.CharField()


class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"
        read_only_fields=["id","created_at","owner"]