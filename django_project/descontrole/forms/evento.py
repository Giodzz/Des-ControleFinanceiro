from django import forms
from ..models import Evento, Categoria
from ..models.enum import NaturezaEnum, TipoEnum
from datetime import datetime


class EventoForm(forms.ModelForm):
    natureza = forms.ChoiceField(
        choices=NaturezaEnum.choices(),
        widget=forms.Select(attrs={"placeholder": "TESTE"}),
        required=True,
    )
    tipo = forms.ChoiceField(choices=TipoEnum.choices())
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(), empty_label=None, required=True
    )

    data = forms.DateField(
        widget=forms.DateInput(attrs={"value": datetime.now().strftime("%d/%m/%Y")}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
        for vf in self.visible_fields():
            vf.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Evento
        fields = ["data", "natureza", "tipo", "categoria", "valor", "descricao"]
