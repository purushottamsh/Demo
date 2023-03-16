from rest_framework import serializers
from .models import Client,CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User=get_user_model()
class ClientSerializer(serializers.ModelSerializer):
    """  serializer for ClientSerializer """

    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Client
        fields = [
            'id',
            'client_name',
            'created_at',
            'updated_at',
            'created_by'
        ]
        read_only_fields = ['created_at']

    def create(self, validated_data):
        logged_in_user = self.context['request'].user
        client = Client.objects.create(created_by=logged_in_user,
                                    **validated_data)
        return client


class ClientDetailSerializer(serializers.ModelSerializer):
    """  serializer for ClientDetailSerializer """

    created_by = serializers.CharField(read_only=True)


    class Meta:
        model = Client
        fields = [
            'id',
            'client_name',
            'projects',
            'created_at',
            'updated_at',
            'created_by'
        ]


class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'project_name'
        ]




class TokenSerializer(serializers.ModelSerializer):
    """  serializer for Token model """

    user=serializers.SerializerMethodField('get_user')

    def get_user(self ,obj):
        """ customize fields for Login API """

        userdata=User.objects.filter(
            id=self.instance.user.id
        ).values ('id','client_name', 'created_at','created_by')

        return userdata

    class Meta:
        model=Token
        fields=['key','user']