from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'
    
    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
    
    def __str__(self):
        return self.title


class Mint(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')

    class Meta:
        verbose_name = 'монетный двор'
        verbose_name_plural = 'монетный двор'
    
    def __str__(self):
        return self.title


class CollectibleItem(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    year = models.IntegerField(blank=True, verbose_name='Год')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    is_on_main = models.BooleanField(default=True, verbose_name='На главной странице')
    
    class Meta:
        abstract = True


class Coin(CollectibleItem):
    
    # Специфичные поля для монет
    denomination = models.CharField(max_length=50, verbose_name='Номинал')  # Номинал (1 рубль, 50 копеек)
    currency = models.CharField(max_length=50, default='RUB', blank=True, null=True, help_text='Например RUB, USD, EUR')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True, null=True)  # Золото, серебро, медь и т.д.
    weight = models.DecimalField(max_digits=8, decimal_places=3, help_text="В граммах", blank=True, null=True)  # Вес
    mint = models.ForeignKey(Mint, on_delete=models.CASCADE, blank=True, null=True) #Монетный двор


    class Meta:
        verbose_name = 'монета'
        verbose_name_plural = 'монет(ы)'
    
    def __str__(self):
        return self.name


class Banknote(CollectibleItem):
    
    # Специфичные поля для банкнот
    denomination = models.CharField(max_length=50, verbose_name='Номинал')  # Номинал
    currency = models.CharField(max_length=50, default='RUB', blank=True, null=True)
    

    class Meta:
        verbose_name = 'банкнота'
        verbose_name_plural = 'банкнот(ы)'
    
    def __str__(self):
        return self.name


