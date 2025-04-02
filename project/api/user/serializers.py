from django.contrib.auth import authenticate

from rest_framework import serializers

from apps.user.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Регистрации пользователя, создания нового."""
    password = serializers.CharField(max_length=128, min_length=3, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

    def create(self, validated_data):
        # Использовать метод create_user из UserManager
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('A email is needed.')
        if password is None:
            raise serializers.ValidationError('A password is needed.')

        # Метод authenticate предоставляется Django
        # email передаем как username, так как USERNAME_FIELD = email.
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('User not found.')
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
