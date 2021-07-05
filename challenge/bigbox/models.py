# Create your models here.
from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    slug = models.SlugField()
    order = models.IntegerField(verbose_name=u'orden',default=0)

    class Meta:
        abstract = True


class Reason(CommonInfo):
    pass


class Category(CommonInfo):
    description = models.TextField(verbose_name=u'descripción')


class Prodcut(models.Model):
    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    description = models.TextField(verbose_name=u'descripción')

    category = models.ForeignKey(Category, verbose_name='categoría', on_delete=models.CASCADE,null=True, blank=True)


    class Meta:
        abstract = True

class Activity(Prodcut):
    reasons = models.ManyToManyField(Reason, verbose_name='tags', blank=True)
    purchase_available = models.BooleanField(
        verbose_name='disponible venta individual', default=False)


class Box(Prodcut):
    activities = models.ManyToManyField(Activity)
    price = models.IntegerField(verbose_name='precio de venta')
    slug = models.CharField(max_length=20, default = ' ')
    purchase_available = models.BooleanField(
        verbose_name='disponible venta individual', default=False)
