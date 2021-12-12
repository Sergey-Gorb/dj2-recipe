
from django.shortcuts import render, redirect
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe(request):

    context = {}
    recipe_name = request.GET.get('name')
    serv = request.GET.get('servings')
    servings = int(serv) if serv else 1
    if recipe_name in DATA:
        ingrs = DATA[recipe_name]
        ingr_dict ={}
        for ingr in ingrs:
            ingr_dict[ingr] = ingrs[ingr] * servings
        context[recipe_name] = ingr_dict
    else:
        context['msg'] = 'Рецепт не выбран!'
    return render(request, 'calculator/index.html', {'recipe': context})