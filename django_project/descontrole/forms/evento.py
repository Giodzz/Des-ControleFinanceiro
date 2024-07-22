from django import forms
from ..models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            "data",
            "natureza",
            "tipo",
            "categoria",
            "valor",
            "descricao"
        ]
