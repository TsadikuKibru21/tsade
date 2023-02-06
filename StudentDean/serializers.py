from rest_framework import serializers
from .models import Block,Dorm
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['Block_name', 'Block_type', 'Block_purpose']


class DormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dorm
        fields = ['Block', 'Dorm_name', 'Capacity','Status']
class UserUploadSerializer(serializers.Serializer):
    file=serializers.FileField()
class SaveFileSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields='__all__'