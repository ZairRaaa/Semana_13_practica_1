from django.db import models


class Tarea(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        COMPLETADA = "completada", "Completada"

    titulo = models.CharField(max_length=150)
    estado = models.CharField(
        max_length=12, choices=Estado.choices, default=Estado.PENDIENTE, db_index=True
    )
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.titulo
