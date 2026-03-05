from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')
    
# "from rest_framework.authtoken.models import Token", "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"]