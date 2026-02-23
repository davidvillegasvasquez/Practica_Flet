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

    #Esta es la función handler. Acepta un único parámetro, en este caso el tipo Mensaje enviado desde su única función o método disparador, pubsub.send_all:
    def enMensaje(mensaje):
    #def enMensaje(mensaje: Mensaje): es más largo pero más descriptivo.
        if mensaje.tipoDeMensaje == "mensaje_chat":
            chat.controls.append(f.Text(f"{mensaje.usuario}: {mensaje.texto}"))
        elif mensaje.tipoDeMensaje == "mensaje_login":
            chat.controls.append(
                f.Text(mensaje.texto, italic=True, color=f.Colors.BLACK_45, size=12)
            ) #El mensaje.texto="{nomUsuario.value} se ha unido al chat."
        pagina.update()

    pagina.pubsub.subscribe(enMensaje) #Parámetro único: la función handler.

    #El nombre arbitrario "eventoX", recibe el objeto del evento, conteniendo detalles del clic. Por lo general se nombra "e" para más limpieza:
    def enviarClick(eventoX):
        pagina.pubsub.send_all(
            Mensaje(
                usuario=pagina.session.store.get("nomUserEnSesion"),
                texto=nuevoMensaje.value,
                tipoDeMensaje="mensaje_chat",
            )
        )
        nuevoMensaje.value = ""

    nomUsuario = f.TextField(label="Introduce tu nombre")

    def unirse_click(e):
        if not nomUsuario.value:
            nomUsuario.error_text = "Nombre no puede ser vacio!"
            pagina.update()
        else:
            pagina.session.store.set("nomUserEnSesion", nomUsuario.value)
            # page.dialog.open = False
            pagina.pop_dialog()
            pagina.pubsub.send_all(
                Mensaje(
                    usuario=nomUsuario.value,
                    texto=f"{nomUsuario.value} se ha unido al chat.",
                    tipoDeMensaje="mensaje_login",
                )
            )

    pagina.show_dialog(
        f.AlertDialog(
            open=True,
            modal=True,
            title=f.Text("Bienvenido!"),
            content=f.Column([nomUsuario], tight=True),
            actions=[f.Button(content="Unirse", on_click=unirse_click)],
            actions_alignment=f.MainAxisAlignment.END,
        )
    )

    pagina.add(
        chat,
        f.ResponsiveRow(controls=[nuevoMensaje, f.Button("Enviar", on_click=enviarClick)]))

f.run(main)
