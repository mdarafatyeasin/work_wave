from rest_framework import serializers
from django.contrib.auth.models import User
from .models import userProfileModel

USER_ROLE = [
    ('employer', 'Post Jobs'),
    ('job_seeker', 'Apply for Jobs'),
]

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfileModel
        fields = '__all__'

class RegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    profile_picture = serializers.ImageField(required=False)
    role = serializers.ChoiceField(choices = USER_ROLE)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'profile_picture', 'role']

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['confirm_password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        profile_picture = validated_data.get('profile_picture')
        role = validated_data['role']

        if password != password2:
            raise serializers.ValidationError({"error": "Password doesn't match"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email already exists"})

        # Create User instance
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        # user.is_active = False
        user.save()

        # Create userProfileModel instance
        profile_data = {'user': user, 'profile_picture': profile_picture, 'role': role}
        userProfileModel.objects.create(**profile_data)

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)