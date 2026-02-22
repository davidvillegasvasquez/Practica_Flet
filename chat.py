from dataclasses import dataclass
import flet as f
#from controles.botones import botonEnviar as send (para tarea).
#from logicas.mensajes import Mensaje

@dataclass
class Mensaje:
    usuario: str
    texto: str
    tipoDeMensaje: str

def main(pagina: f.Page):
    #Para hacer responsivo y se vea bien en smar
    pagina.title = "Pepis Chat"
    pagina.adaptive = True  # Mejora el look and feel nativo
    pagina.scroll = "auto"  # Permite scroll si el contenido es largo

    chat = f.Column()
    nuevoMensaje = f.TextField()

    def enMensaje(mensaje: Mensaje):
        if mensaje.tipoDeMensaje == "mensaje_chat":
            chat.controls.append(f.Text(f"{mensaje.usuario}: {mensaje.texto}"))
        elif mensaje.tipoDeMensaje == "mensaje_login":
            chat.controls.append(
                f.Text(mensaje.texto, italic=True, color=f.Colors.BLACK_45, size=12)
            )
        pagina.update()

    pagina.pubsub.subscribe(enMensaje)

    #El nombre arbitrario "eventoX", recibe el objeto del evento, conteniendo detalles del clic. Por lo general se nombra "e" para más limpieza:
    def enviarClick(eventoX):
        pagina.pubsub.send_all(
            Mensaje(
                usuario=pagina.session.store.get("nombre_usuario"),
                texto=nuevoMensaje.value,
                tipoDeMensaje="mensaje_chat",
            )
        )
        nuevoMensaje.value = ""

    nombre_usuario = f.TextField(label="Introduce tu nombre")

    def unirse_click(e):
        if nombre_usuario.value:
            nombre_usuario.error_text = "Nombre no puede ser vacio!"
        else:
            pagina.session.store.set("nombre_usuario", nombre_usuario.value)
            # page.dialog.open = False
            pagina.pop_dialog()
            pagina.pubsub.send_all(
                Mensaje(
                    usuario=nombre_usuario.value,
                    texto=f"{nombre_usuario.value} se ha unido al chat.",
                    tipoDeMensaje="mensaje_login",
                )
            )

    pagina.show_dialog(
        f.AlertDialog(
            open=True,
            modal=True,
            title=f.Text("Bienvenido!"),
            content=f.Column([nombre_usuario], tight=True),
            actions=[f.Button(content="Unirse", on_click=unirse_click)],
            actions_alignment=f.MainAxisAlignment.END,
        )
    )

    pagina.add(
        chat,
        f.ResponsiveRow(controls=[nuevoMensaje, f.Button("Enviar", on_click=enviarClick)]),
    )

f.run(main)
