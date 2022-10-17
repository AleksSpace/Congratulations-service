from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from people.forms import CongratulationForm, PeopleForm
from people.models import Congratulation, People


class CongratulationListView(ListView):
    """Класс показывает список поздравлений"""
    model = Congratulation
    template_name = 'congratulation/texts.html'
    context_object_name = 'texts'


class CreateCongratulationView(CreateView):
    """Класс для создания поздравлений"""
    form_class = CongratulationForm
    template_name = 'congratulation/create_text_form.html'
    success_url = reverse_lazy('text')


class DetailCongratulationView(DetailView):
    """Класс для просмотра конкретного поздравления"""
    model = Congratulation
    template_name = 'congratulation/text_detail.html'
    context_object_name = 'text_item'


class UpdateCongratulationView(UpdateView):
    """Класс для редактирования конкретного поздравления"""
    model = Congratulation
    form_class = CongratulationForm
    template_name = 'congratulation/create_text_form.html'
    context_object_name = 'text_item'
    success_url = reverse_lazy('text')


class DeleteCongratulationView(DeleteView):
    """Класс для удаления конкретного поздравления"""
    model = Congratulation
    context_object_name = 'text_item'
    success_url = reverse_lazy('text')
    template_name = 'congratulation/text_delete.html'


class PeopleListView(ListView):
    """Класс показывает список сотрудников"""
    model = People
    template_name = 'people/people.html'
    context_object_name = 'people'


class CreatePeopleView(CreateView):
    """Класс для создания сотрудника"""
    form_class = PeopleForm
    template_name = 'people/create_people_form.html'
    success_url = reverse_lazy('people')


class UpdatePeopleView(UpdateView):
    """Класс для редактирования конкретного сотрудника"""
    model = People
    form_class = PeopleForm
    template_name = 'people/create_people_form.html'
    context_object_name = 'people_item'
    success_url = reverse_lazy('people')


class DeletePeopleView(DeleteView):
    """Класс для удаления конкретного сотрудника"""
    model = People
    context_object_name = 'people_item'
    success_url = reverse_lazy('people')
    template_name = 'people/people_delete.html'


# class DownloadCongratulations():

#     def download_text(self, request):
#         response = HttpResponse(content_type='text/plain')
#         response['Content-Disposition'] = 'attachment; filename="Поздравление.docs"'

#         lines = [
#             "test print text 1\n",
#             "test print text 2\n",
#             "test print text 3\n",
#         ]

#         response.writelines(lines)
#         return response
