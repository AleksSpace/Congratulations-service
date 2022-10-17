from django.urls import path
from people.utils import download_text
from people.views import (CongratulationListView, CreateCongratulationView,
                          CreatePeopleView, DeleteCongratulationView,
                          DeletePeopleView, DetailCongratulationView,
                          PeopleListView, UpdateCongratulationView,
                          UpdatePeopleView)

urlpatterns = [
    path('', PeopleListView.as_view(), name='people'),
    path('text/', CongratulationListView.as_view(), name='text'),
    path('add-text/', CreateCongratulationView.as_view(), name='add_text'),
    path('text/<int:pk>/', DetailCongratulationView.as_view(), name='text_detail'),
    path('update-text/<int:pk>/', UpdateCongratulationView.as_view(), name='text_update'),
    path('delete-text/<int:pk>/', DeleteCongratulationView.as_view(), name='text_delete'),
    path('add-people/', CreatePeopleView.as_view(), name='add_people'),
    path('people-update/<int:pk>/', UpdatePeopleView.as_view(), name='people_update'),
    path('people-delete/<int:pk>/', DeletePeopleView.as_view(), name='people_delete'),
    path('download/<int:pk>/', download_text, name='download'),
]
