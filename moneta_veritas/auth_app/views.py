import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Profile


@csrf_exempt
@require_http_methods(["POST"])
def check_user_exists(request):
    """Проверяет существование пользователя"""
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()

        user_exists = User.objects.filter(username=username).exists()

        return JsonResponse({
            'exists': user_exists,
            'username': username
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def login_user(request):
    """Выполняет вход пользователя"""
    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                'success': True,
                'message': 'Вход выполнен успешно'
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Неверный логин или пароль'
            })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def register_user(request):
    """Регистрирует нового пользователя"""
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')

        # Валидация
        if not username or not password:
            return JsonResponse({
                'success': False,
                'error': 'Логин и пароль обязательны'
            })

        if password != confirm_password:
            return JsonResponse({
                'success': False,
                'error': 'Пароли не совпадают'
            })

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                'success': False,
                'error': 'Пользователь с таким логином уже существует'
            })

        # Создаем пользователя
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Профиль создается автоматически через сигналы

        # Автоматически входим после регистрации
        login(request, user)

        return JsonResponse({
            'success': True,
            'message': 'Регистрация выполнена успешно'
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@require_http_methods(["POST"])
def logout_user(request):
    """Выход пользователя"""
    logout(request)
    return JsonResponse({'success': True})