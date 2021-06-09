from django.db import models


class Theatre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название театра')
    place = models.CharField(max_length=20, verbose_name='Местоположение театра')

    class Meta:
        verbose_name = 'Театр'
        verbose_name_plural = 'Театр'

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название мероприятия')
    visitors = models.IntegerField(verbose_name='Количество посетителей')
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, max_length=20,
                                verbose_name='В каком театре проводится')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятие'

    def __str__(self):
        return self.name


class Visitor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Ф.И.О')
    age = models.IntegerField(verbose_name='Возраст')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, max_length=20, verbose_name='Какое мероприятие посещал(а)')

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетитель'

    def __str__(self):
        return self.name
