from dataclasses import field
from distutils.command.upload import upload
import profile
from wsgiref.validate import validator
from rest_framework import serializers
from apps.users.models import User 
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'phone', 'profile_image')

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'profile_image')

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    phone = serializers.CharField(required = True)
    profile_image = serializers.ImageField()
    password1 = serializers.CharField(write_only = True,required = True, validators =[validate_password])
    password2 = serializers.CharField(write_only = True,required = True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name','last_name', 'phone', 'profile_image')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            phone = validated_data['phone'],
            profile_image = validated_data['profile_image']
        )

        user.set_password(validated_data['password1'])
        user.save()

        return user 