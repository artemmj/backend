import jwt

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import authentication, exceptions

User = get_user_model()


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None
        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """Попытка аутентификации с предоставленными данными."""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        except Exception as exc:
            raise exceptions.AuthenticationFailed(f'Ошибка аутентификации. Невозможно декодировать токен. {exc}')

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Пользователь соответствующий данному токену не найден.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Данный пользователь деактивирован.')

        return (user, token)
