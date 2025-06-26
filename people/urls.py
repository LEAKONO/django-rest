from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.get_all_people, name='get_all_people'),
    path('people/create/', views.create_person, name='create_person'),
    path('people/<int:pk>/delete/', views.delete_person, name='delete_person'),
    path('people/<int:pk>/update/', views.update_person, name='update_person'),
]
