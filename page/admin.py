from django.contrib import admin
from .models import Category, Good
from page.models import Good,Category





class GoodAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(Category,CategoryAdmin)
admin.site.register(Good,GoodAdmin)
