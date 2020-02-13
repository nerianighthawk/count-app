from django.shortcuts import render
from .models import Count


def index(request):
    count_instances_num = Count.objects.all().count()
    context = {'count': count_instances_num}
    return render(request, 'index.html', context)


def plus(request):
    count_instance = Count.objects.create()
    count_instance.save()
    count_instances_num = Count.objects.all().count()
    context = {'count': count_instances_num}
    return render(request, 'index.html', context)
