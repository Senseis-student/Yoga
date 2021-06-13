from django.db import models


class Program(models.Model):
    title = models.CharField('Название программы', max_length=50)
    description = models.CharField('Описание программы',max_length=300)
    text = models.TextField(blank=True)
    img = models.ImageField('Изображение', blank=True, upload_to='program/')

    def __str__(self): 
        return self.title

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'

class Price (models.Model):
    title = models.CharField('Название курса', max_length=50)
    price = models.CharField('Цена', max_length=50)
    program_price = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self): 
        return self.title

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'



