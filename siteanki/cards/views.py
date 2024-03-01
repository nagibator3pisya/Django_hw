from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render


def catalog(requrest):
    return HttpResponse("Каталог карточек")



def get_card_by_id(requrest, card_id):
    return HttpResponse(f"Карточка "
                        f"<p> id:{card_id}</p>")



def get_category_by_name(requrest, slug):
    return HttpResponse(f"Категория "
                        f"<p> slug: {slug}</p>")




# Станица не найдена
def page_not_fount(requrest,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')