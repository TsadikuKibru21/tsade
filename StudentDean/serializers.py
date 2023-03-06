from rest_framework import serializers
from .models import Block,Dorm,Placement
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
        
class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['Stud_id', 'FirstName', 'LastName','block','room']

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