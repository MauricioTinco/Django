from django import forms
from .models import TrainingDay

class TrainingDayForm(forms.ModelForm):
    class Meta:
        model = TrainingDay
        fields = ['date', 'routine_type', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'routine_type': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ej. Buenas sensaciones en el sparring o récord en sentadillas...'}),
        }