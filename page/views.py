from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Category, Good


def index(request, cat_id):
    try:
        cat = Category.objects.get(pk=cat_id)
    except Category.DoesNotExist:
        raise Http404
    # if cat_id == None:
    #     cat = Category.objects.first()
    # else:
    Category.objects.get(pk=cat_id)
    goods = Good.objects.filter(category=cat).order_by("name")
    s = str(cat_id) + " Категория: " + cat.name + "<br> <br>"
    for good in goods:
        s += "(" + str(good.pk) + ") " + good.name + "<br>"
    return HttpResponse(s)


def good(request, good_id):
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404
    s = good.name + "<br> <br>" + good.category.name + "<br><br>" + good.description
    if not good.in_stock:
        s += "<br><br>" + " Нет в наличии!"
    return HttpResponse(s)
