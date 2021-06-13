from django.db import models


class Branches(models.Model):
    address = models.CharField('Адрес филиала',max_length=300)
    number = models.CharField('Номер телефона', max_length=15)
    text = models.TextField(blank=True)

    def __str__(self): 
        return self.address

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'