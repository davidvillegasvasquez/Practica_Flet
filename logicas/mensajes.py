from dataclasses import dataclass

@dataclass
class Mensaje:
    usuario: str
    texto: str
    tipoDeMensaje: str