from django import forms
from people.models import Congratulation, People

CHOICES = (
    ('woman', 'Женский'),
    ('man', 'Мужской'),
)


class PeopleForm(forms.ModelForm):
    """Форма для сохранения сотрудников"""
    class Meta:
        model = People
        fields = ('gender', 'last_name', 'first_name', 'patronymic')
        widgets = {
            'gender': forms.Select(choices=CHOICES,
                                   attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Напишите фамилию сотрудника'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Напишите имя сотрудника'}),
            'patronymic': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Напишите отчество сотрудника'}),
        }


class CongratulationForm(forms.ModelForm):
    """Форма для сохранения текстов поздравлений"""
    class Meta:
        model = Congratulation
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'rows': 10,
                                          'placeholder': 'Напишите текст здесь'
                                          }),
        }
