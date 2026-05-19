from django.urls import path
from .views import TrainingListView, TrainingCreateView, TrainingUpdateView

urlpatterns = [
    path('', TrainingListView.as_view(), name='training-list'),
    path('nuevo/', TrainingCreateView.as_view(), name='training-create'),
    path('editar/<int:pk>/', TrainingUpdateView.as_view(), name='training-update'),
]