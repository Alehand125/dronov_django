from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="В наличии")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Категория")
    price = models.FloatField(default=0, verbose_name="Цена за единицу")
    description = models.TextField(default=" ", verbose_name="Описание товара")

    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price", "description")
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"

    def get_in_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s += " (нет в наличии)"
        return s

    def save(self, *args, **kwargs):
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Good, self).delete(*args, **kwargs)


class BlogArticle(models.Model):
    title = models.CharField(max_length=100, unique_for_date="pubdate")
    pubdate = models.DateField()
    update = models.DateTimeField(auto_now=True)
