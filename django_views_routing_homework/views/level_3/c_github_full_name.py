"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

from django.http import JsonResponse, HttpResponse, HttpRequest
import requests
import json

from constant import TOKEN


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> HttpResponse:
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {TOKEN}',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    url = f'https://api.github.com/users/{github_username}'

    response = requests.get(url, headers=headers)
    if response:
        try:
            user_info = response.json()
        except ValueError:
            return HttpResponse('Ошибка данных')
    else:
        return HttpResponse(status=404)
    
    name_user = user_info['name']
    if name_user:
        return JsonResponse(data={"name": name_user})
    return HttpResponse(None)
