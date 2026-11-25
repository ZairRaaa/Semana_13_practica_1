from rest_framework import serializers

from .models import Tarea


class TareaSerializer(serializers.HyperlinkedModelSerializer):
    estado_texto = serializers.ReadOnlyField(source="get_estado_display")
    duracion_dias = serializers.SerializerMethodField()

    class Meta:
        model = Tarea
        fields = (
            "id", "url", "titulo", "estado", "estado_texto",
            "fecha_inicio", "fecha_limite", "duracion_dias",
        )

    def get_duracion_dias(self, tarea: Tarea) -> int:
        """Días transcurridos entre el inicio y la fecha límite."""
        return (tarea.fecha_limite - tarea.fecha_inicio).days

    def validate(self, attrs):
        inicio = attrs.get("fecha_inicio", getattr(self.instance, "fecha_inicio", None))
        limite = attrs.get("fecha_limite", getattr(self.instance, "fecha_limite", None))
        if inicio is not None and limite is not None and limite < inicio:
            raise serializers.ValidationError({
                "fecha_limite": "La fecha límite debe ser igual o posterior a la fecha de inicio."
            })
        return attrs
