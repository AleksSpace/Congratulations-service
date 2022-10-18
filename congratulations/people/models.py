from django.db import models

MAN = 'Мужской'
WOMAN = 'Женский'

GENDER = (
    (MAN, 'Мужской'),
    (WOMAN, 'Женский'),
)


class People(models.Model):
    gender = models.CharField(max_length=9,
                              choices=GENDER,
                              default='Женский',
                              verbose_name='Пол')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')

    class Meta:
        verbose_name = "Именинник"
        verbose_name_plural = "Именинники"
        ordering = ['last_name']

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic


class Congratulation(models.Model):
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = "Текст поздравления"
        verbose_name_plural = "Тексты поздравлений"

    def __str__(self):
        return self.text
