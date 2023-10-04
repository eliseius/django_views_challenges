"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.http import HttpResponse, HttpRequest
from pathlib import Path

import random
import pathlib


def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    length = request.GET.get('length')
    
    if length is None or int(length) > 10000:
        return HttpResponse(status=403)
    
    text = get_text(int(length))

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="exsample.txt"'},
    )

    response.write(text)
    return response


def get_list_words(name_file: str) -> list[str]:
    with open(name_file, encoding='utf-8') as file:
        text = file.read()
    return text.split()


def make_pairs(data: list[str]) -> tuple:
    for item in range(len(data)-1):
        yield (data[item], data[item+1])


def make_words_dict(data: list[str]) -> dict[str, list[str]]:
    words_dict = {}

    for word_1, word_2 in make_pairs(data):
        if word_1 in words_dict.keys():
            words_dict[word_1].append(word_2)
        else:
            words_dict[word_1] = [word_2]
    return words_dict


def get_first_word(words_list: list[str]) -> str:
    word = random.choice(words_list)
    while word.islower():
        word = random.choice(words_list)
    return word


def get_text(numb: int) -> str:
    path = Path(pathlib.Path.home(), 'Загрузки', 'che.txt')
    words_list = get_list_words(path)
    words_dict = make_words_dict(words_list)
    first_word = get_first_word(words_list)
    chain = [first_word]

    for _ in range(numb-1):
        last_word_chain = chain[-1]
        words_for_choice = words_dict[last_word_chain]
        chain.append(random.choice(words_for_choice))

    return ' '.join(chain)