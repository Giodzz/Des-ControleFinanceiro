from enum import Enum


class NaturezaEnum(Enum):
    SAIDA = "saida"
    ENTRADA = "entrada"

    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls]
    
    class Meta:
        app_label = 'descontrole'

class TipoEnum(Enum):
    PIX = "pix"
    DEBITO = "debito"
    CREDITO = "credito"
    DINHEIRO = "dinheiro"
    BOLETO = "boleto"
    OUTROS = "outros"

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace("_", " ").capitalize()) for key in cls]
    

    class Meta:
        app_label = 'descontrole'