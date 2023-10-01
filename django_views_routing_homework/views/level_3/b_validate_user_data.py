"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""

import json

from django.http import JsonResponse, HttpResponse, HttpRequest

from django_views_routing_homework.models import User


def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            return HttpResponse('bad request')
    else:
        return HttpResponse()
    
    response = check_conditions(data)
    return JsonResponse(data={'is_valid': response}, status=200)


def check_conditions(data):
    check = User.objects.create(
        full_name=data['full_name'],
        email=data['email'],
        registered_from=data['registered_from'],
        age=data['age']
    )
    if check:
        return True
    else:
        return False
