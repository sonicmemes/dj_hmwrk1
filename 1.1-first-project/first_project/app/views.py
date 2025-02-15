import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # Получаем текущую рабочую директорию
    current_dir = os.getcwd()

    # Получаем список файлов в директории
    files = os.listdir(current_dir)

    # Формируем строку с именами файлов
    file_names = "\n".join(files)

    return HttpResponse(f'Список файлов в рабочей директории:\n{file_names}')
