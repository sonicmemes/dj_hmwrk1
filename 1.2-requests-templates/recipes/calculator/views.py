from django.shortcuts import render

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


def recipe_view(request, recipe_name):
    # Получаем данные для указанного рецепта
    recipe_data = DATA.get(recipe_name, {})
    servings = request.GET.get('servings', 1)

    # Умножаем количество ингредиентов на количество порций
    original_recipe_data = recipe_data.copy()

    recipe_data = original_recipe_data.copy()

    for ingredient, amount in recipe_data.items():
        try:
            recipe_data[ingredient] = float(amount) * int(servings)
        except ValueError:
            pass  # Пропускаем
    # Создаем контекст для передачи в шаблон
    context = {'recipe': recipe_data}
    recipe_data = original_recipe_data.copy()
    # Отображаем шаблон с контекстом
    return render(request, 'calculator/index.html', context)
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
