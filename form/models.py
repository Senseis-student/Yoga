from django.db import models
from program.models import Program 
from branches.models import Branches


class Form(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    scale = models.IntegerField('Возраст')
    categories = (
        ('W', 'Женский'),
        ('M', 'Мужской'),
    )
    pol = models.CharField('Пол', choices=categories, max_length=1)
    number = models.CharField('Номер телефона', max_length=15)
    email = models.EmailField('Почта', max_length=150)
    bran = models.ForeignKey(Branches, on_delete=models.CASCADE)
    prog = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'