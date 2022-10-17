import io
import os
import random

from django.conf import settings
from django.http import FileResponse
from docxtpl import DocxTemplate
from people.models import Congratulation, People


def randon_congratulation():
        """Функция выбирает случайный текст поздравления из тех что есть в базе"""
        congratulation = Congratulation.objects.all()
        rundom_congratulation = random.choice(congratulation)
        rundom_congratulation_str = str(rundom_congratulation)

        return rundom_congratulation_str


def download_text(request, pk):        
    man = People.objects.filter(id=pk)
    first_name = man[0].first_name
    last_name = man[0].last_name
    if man[0].gender == 'Женский':
        lines = f'Дорогая {first_name}!'
        document = 'document_women.docx'
    if man[0].gender == 'Мужской':
        lines = f'Дорогой {first_name}!'
        document = 'document_men.docx'

    context = {'name' : lines, 'text': randon_congratulation()}
    byte_io = io.BytesIO()
    tpl = DocxTemplate(os.path.join(settings.BASE_DIR, 'people', 'templates', 'docx_report', document))
    tpl.render(context)
    tpl.save(byte_io)
    byte_io.seek(0)
    return FileResponse(byte_io, as_attachment=True, filename=f'Поздравление_{last_name}.docx')