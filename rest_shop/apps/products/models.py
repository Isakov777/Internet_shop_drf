from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save
from apps.categories.models import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название продукта')
    description = models.TextField(blank=True, null=True, verbose_name='Описание  продукта')
    price = models.PositiveIntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    is_stock = models.BooleanField(default=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-id']

    def get_parent(self):
        return self.category.filter(parent__isnull=True)

class ProductImage(models.Model):
    image = models.ImageField(upload_to = 'product', verbose_name = 'Картинка', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product')

    def __str__(self) -> str:
        return self.product.title

    