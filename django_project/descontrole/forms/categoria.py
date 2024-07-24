from django import forms
from ..models import Categoria


class CategoriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)

    class Meta:
        model = Categoria
        fields = ["nome", "descricao"]
