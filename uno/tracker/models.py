from django.db import models

class TrainingDay(models.Model):
    TRAINING_CHOICES = [
        ('hipertrofia', 'Pesas (Hipertrofia)'),
        ('mma', 'Clases de MMA'),
        ('descanso', 'Día de Descanso'),
    ]
    
    date = models.DateField(unique=True, verbose_name="Fecha")
    routine_type = models.CharField(max_length=20, choices=TRAINING_CHOICES, verbose_name="Tipo de Rutina")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas del Día")

    def __str__(self):
        return f"{self.date} - {self.get_routine_type_display()}"

class Supplementation(models.Model):
    training_day = models.ForeignKey(TrainingDay, on_delete=models.CASCADE, related_name='supplements')
    protein_grams = models.PositiveIntegerField(default=0, verbose_name="Proteína (g)")
    creatine_grams = models.PositiveIntegerField(default=0, verbose_name="Creatina (g)")

    def __str__(self):
        return f"Suplementos - {self.training_day.date}"