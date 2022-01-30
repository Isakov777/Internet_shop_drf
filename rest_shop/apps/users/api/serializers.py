from django.db.models import fields
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'profile', 'age',  'password'
        )

        def create(self, validated_data):
            user = super().create(validated_data)
            password = validated_data['password']
            user.set_password(password)
            user.save()
            return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'age',  'password')