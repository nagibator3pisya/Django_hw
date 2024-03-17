from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
info = {'users_count': 100500, 'cards_count': 200600, 'menu': [
    {"title": "Главная",
     "url": "/",
     "url_name": "index"},
    {"title": "О проекте",
     "url": "/about/",
     "url_name": "about"},
    {"title": "Каталог",
     "url": "/cards/catalog/",
     "url_name": "catalog"},
], 'cards': 'cards_dataset'}

cards_dataset = [
    {'question': "Что такое PEP 8?",
     "answer": "PEP 8 — стандарт написания кода на Python.",
     "category": "Стандарты кода",
     "tags": ["PEP 8", "стиль", "форматирование"],
     "id_author": 1,
     "id_card": 1,
     "upload_date": "2023-01-15",
     "views_count": 100,
     "favorites_count": 25
     },
    {"question": "Как объявить список в Python?",
     "answer": "С помощью квадратных скобок: lst = []",
     "category": "Основы",
     "tags": ["списки", "основы"],
     "id_author": 2,
     "id_card": 2,
     "upload_date": "2023-01-20",
     "views_count": 150,
     "favorites_count": 30
     },
    {"question": "Что делает метод .append()?",
     "answer": "Добавляет элемент в конец списка.",
     "category": "Списки",
     "tags": ["списки", "методы"],
     "id_author": 2,
     "id_card": 3,
     "upload_date": "2023-02-05",
     "views_count": 75,
     "favorites_count": 20
     },
    {"question": "Какие типы данных в Python иммутабельные?",
     "answer": "Строки, числа, кортежи.",
     "category": "Типы данных",
     "tags": ["типы данных", "иммутабельность"],
     "id_author": 1,
     "id_card": 4,
     "upload_date": "2023-02-10",
     "views_count": 90,
     "favorites_count": 22
     },
    {"question": "Как создать виртуальное окружение в Python?",
     "answer": "С помощью команды: python -m venv myenv",
     "category": "Виртуальные окружения",
     "tags": ["venv", "окружение"],
     "id_author": 2,
     "id_card": 5,
     "upload_date": "2023-03-01",
     "views_count": 120,
     "favorites_count": 40
     }
]


def main(request):
    data = {
        'title': "Главная станица",
        'cards': cards_dataset
    }
    return render(request, "main.html", context=data)


def about(request):
    return render(request, 'about.html', {'title': 'О сайте'})


def card_details(request, card_id):

    card = next((card for card in cards_dataset if card['id_card'] == card_id), None)

    if card:
        return render(request, 'card_details.html', {'card': card, 'title': "Детали Карты"})
    else:
        return page_not_fount(request, None)




# Станица не найдена
def page_not_fount(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
