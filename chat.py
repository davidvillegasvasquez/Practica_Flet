from dataclasses import dataclass
import flet as f
#from controles.botones import botonEnviar as send (para tarea).

@dataclass
class Mensaje:
    usuario: str
    texto: str

def main(pagina: f.Page):
    pagina.title = "Pepis Chat"
    pagina.adaptive = True  # Mejora el look and feel nativo
    pagina.scroll = "auto"  # Permite scroll si el contenido es largo
    chat = f.Column()
    nuevoMensaje = f.TextField()

    def enMensaje(mensaje: Mensaje):
        chat.controls.append(f.Text(f"{mensaje.usuario}: {mensaje.texto}"))
        pagina.update()

    pagina.pubsub.subscribe(enMensaje)

    #El nombre arbitrario "eventoX", recibe el objeto del evento, conteniendo detalles del clic. Por lo general se nombra "e" para más limpieza:
    def enviarClick(eventoX):
        pagina.pubsub.send_all(Mensaje(usuario = pagina.session.id, texto = nuevoMensaje.value))
        nuevoMensaje.value = ""

    pagina.add(
        chat,
        f.ResponsiveRow(controls=[nuevoMensaje, f.Button("Enviar", on_click=enviarClick)]),
    )

f.run(main)
