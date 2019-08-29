from django.db import models


class District(models.Model):
    name = models.CharField('Название', max_length=50, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Category(models.Model):
    name = models.CharField('Название', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Network(models.Model):
    name = models.CharField('Название', max_length=40, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сеть предприятий'
        verbose_name_plural = 'Сети предприятий'


class Organization(models.Model):
    network = models.ForeignKey(Network, related_name='organization', verbose_name="Сеть", null=True, blank=False,
                                on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=256, null=True)
    districts = models.ManyToManyField(District, related_name='organizations', verbose_name='Районы')

    def __str__(self):
        return f'{self.network.name} #{self.id}'

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'


class Product(models.Model):
    name = models.CharField('Название', max_length=40, blank=False)
    category = models.ForeignKey(Category, related_name='product', verbose_name='Категория', on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return f'{self.category.name} {self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='product_price', verbose_name='Продукт',
                                on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='product_price', verbose_name='Предприятие',
                                on_delete=models.CASCADE, null=False)
    price = models.DecimalField('Цена', blank=False, decimal_places=2, max_digits=9)

    class Meta:
        verbose_name = 'Цена на продукт'
        verbose_name_plural = 'Цены на продукты'
