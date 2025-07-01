from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Стоимость товара")
    discounted_price = models.PositiveIntegerField(
        verbose_name="Стоимость товара со скидкой"
    )
    rating = models.FloatField( verbose_name="Рейтинг")
    reviews = models.PositiveIntegerField(verbose_name="Количество отзывов")

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return str(self.title)
