from django.shortcuts import render
import datetime


def layout(request):
    return render(request, 'layout.html')


def indexs(request):
    return render(request, 'indexs.html')


def it(request):
    return render(request, 'it.html')


def con(request):
    return render(request, 'togglebar.html')