from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='img_product', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена', **NULLABLE)
    created_at = models.DateField(verbose_name='дата создания', **NULLABLE)
    updated_at = models.DateField(verbose_name='дата обновления', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Товары'  # Настройка для наименования набора объектов


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(default=0, verbose_name='номер версии')
    name = models.CharField(max_length=100, verbose_name='название версии')
    attribute_bul = models.BooleanField(default=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} №{self.number}'

    class Meta:
        verbose_name = 'Версия'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Версии'  # Настройка для наименования набора объектов
