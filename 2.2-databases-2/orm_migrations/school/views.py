from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Prefetch


from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    object_list = Student.objects.all().order_by(ordering)

    context = {'object_list': object_list}


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
