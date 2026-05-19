from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import TrainingDay
from .forms import TrainingDayForm
from django.shortcuts import redirect

class TrainingListView(ListView):
    model = TrainingDay
    template_name = 'tracker/training_list.html'
    context_object_name = 'trainings'
    ordering = ['-date']  # Muestra el día más reciente primero

class TrainingCreateView(CreateView):
    model = TrainingDay
    form_class = TrainingDayForm
    template_name = 'tracker/training_form.html'
    success_url = reverse_lazy('training-list')

class TrainingUpdateView(UpdateView):
    model = TrainingDay
    form_class = TrainingDayForm
    template_name = 'tracker/training_form.html'
    success_url = reverse_lazy('training-list')

def error_404_redirect(request, exception):
    return redirect('/')  # Redirige automáticamente a la raíz del sitio