from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Category, Good
from django.core.paginator import Paginator, InvalidPage  # чтобы страницы выводились с разбивкой


def index(request, cat_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    if cat_id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=cat_id)
    cats = Category.objects.all().order_by("name")
    goods = Good.objects.filter(category=cat).order_by("name")
    paginator = Paginator(Good.objects.filter(category=cat).order_by("name"), 10)
    # s = " Категория: " + cat.name + "<br> <br>"
    # for good in goods:
    #     s = s + good.name + "  " + str(good.price) + "<br>"
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)
    return render(request, "index.html", {"category": cat, "cats": cats, "goods": goods})


def good(request, good_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404

    # s = good.name + "<br> <br>" + good.category.name + "<br><br>" + good.description
    # if not good.in_stock:
    #     s += "<br><br>" + " Нет в наличии!"
    return render(request, "good.html", {"good": good, "cats": cats,"pn":page_num})
