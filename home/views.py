from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    context = {}

    return render(request, 'home/index.html', context)

def events(request):
    context = {}

    return render(request, 'home/events.html', context)

def termninal(request):
    context = {}

    return render(request, 'home/terminal.html', context)