from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from .models import Category, Good
from django.http import Http404
from django.views.generic.list import ListView


# class GoodListView(TemplateView):
class GoodListView(ListView):
    template_name = "index.html"
    paginate_by = 10
    cat = None

    def get(self,request, *args,**kwargs):
        if (self.kwargs["cat_id"]==None):
            self.cat=Category.objects.first()
        else:
            self.cat = Category.objects.get(pk=self.kwargs["cat_id"])
        return super(GoodListView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        # try:
        #     page_num = self.request.GET["page"]
        # except KeyError:
        #     page_num = 1
        context["cats"] = Category.objects.order_by("name")
        context["category"] = self.cat
        # if kwargs["cat_id"] == None:
        #     context["category"] = Category.objects.first()
        # else:
        #     context["category"] = Category.objects.get(pk=kwargs["cat_id"])

        # paginator = Paginator(Good.objects.filter(category=context["category"]).order_by("name"),
        #                       10)  # в учебнике тут ошщибка
        # try:
        #     context["goods"] = paginator.page(page_num)
        # except InvalidPage:
        #     context["goods"] = paginator.page(1)
        return context

    def get_queryset(self):
        return Good.objects.filter(category=self.cat).order_by("name")

class GoodDetailView(TemplateView):
    template_name = "good.html"

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = 1
        context["cats"] = Category.objects.order_by("name")
        try:
            context["good"] = Good.objects.get(pk=kwargs["good_id"])
        except Good.DoesNotExist:
            raise Http404
        return context
