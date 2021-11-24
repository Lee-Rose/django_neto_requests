from django.shortcuts import render
from django.http import HttpResponse
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
    'milkshake': {
        'молоко, мл': 0.25,
        'ягоды, г': 0.05,
        'фрукты, г': 0.1,
    },
}


def index_view(request, sign_recipe, servings=1):
    ''' get recipe in calculated portions '''

    description = DATA.get(sign_recipe, None)
    servings = int(request.GET.get('servings', int(1)))
    if description:
        context_rec = {}
        context = {
            'recipe': context_rec
        }
        if sign_recipe in DATA.keys():
            context_rec[sign_recipe] = DATA[sign_recipe]

            for item, value in context_rec.items():
                for i, count in value.items():
                    context_rec[item][i] = round((count) * servings, 3)

            return render(request, 'calculator/index.html', context=context)
    else:
        return HttpResponse(f'Рецепта {sign_recipe} я не знаю.')


def all_recipe(request):

    return HttpResponse(content=DATA)

def home_view(request):

    return HttpResponse(f"<a href={reverse('all_rec')}> <h1>Рецепты</a4> </h1>")


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
