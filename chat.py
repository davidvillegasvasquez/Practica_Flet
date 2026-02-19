import flet as f
#from controles.botones import botonEnviar as send (para tarea).

def main(pagina: f.Page):
    chat = f.Column()
    nuevoMensaje = f.TextField()

    #El nombre arbitrario "eventoX", recibe el objeto del evento, conteniendo detalles del clic. Por lo general se nombra "e" para más limpieza:
    def enviarClick(eventoX):
        chat.controls.append(f.Text(nuevoMensaje.value))
        nuevoMensaje.value = ""

    pagina.add(
        chat,
        f.Row(controls=[nuevoMensaje, f.Button("Enviar", on_click=enviarClick)]),
    )

f.run(main)