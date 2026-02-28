from dataclasses import field
import flet as f

@dataclass
class Tarea:  # noqa: B903
    texto: str

@f.control
class LineaDeTarea():
    def __init__(self, tarea: Tarea):
        super().__init__()
        self.message = message
        self.vertical_alignment = f.CrossAxisAlignment.START
        self.controls = [
            f.Row(
                tight=True,
                spacing=5,
                controls=[
                    #f.CheckBox(),
                    f.Text(self.tarea.text, selectable=True),
                    #f.IconoLapicero(),
                    #f.IconoPapelera,
                ],
            ),
        ]

def main(pagina: f.Page):
    pagina.title = "Para Hacer"
    encabezado = f.Text(value="Tareas", color=f.Colors.WHITE, size=40, alignment=f.MainAxisAlignment.CENTER)
    nuevaTarea = f.TextField()
    listaDeTareas = f.Column()

    def clickEnMenuTodasActivasCompletadas(eventoMenuTodActiComple):
        # eventoMenuTodActiComple.control es el texto que fue clickeado
        eventoMenuTodActiComple.control.color = "blue"
        eventoMenuTodActiComple.control.weight = "bold"
        eventoMenuTodActiComple.control.decoration = f.TextDecoration.UNDERLINE
        eventoMenuTodActiComple.control.update() # Actualiza el elemento en pantalla

    # Crear los textos con propiedades iniciales
    todas = f.Text("Todas", size=20, color="black", on_click=clickEnMenuTodasActivasCompletadas)

    activas = f.Text("Activas", size=20, color="black", on_click=clickEnMenuTodasActivasCompletadas)

    completadas = f.Text("Completadas", size=20, color="black", on_click=clickEnMenuTodasActivasCompletadas)

    def ingresarTarea(eventoX):
        #tarea = Tarea(texto=nuevaTarea.value)
        listaDeTareas.controls.append(
            LineaDeTarea(Tarea(texto=nuevaTarea.value))     
        )
       
        nuevaTarea.value = ""
        pagina.update()

    pagina.add(
        f.Column(
            controls=[
                f.Row(
                    controls=[
                        encabezado,
                    ]
                ),
                f.Row(
                    controls=[
                        nuevaTarea,
                        f.Button("+", on_click=ingresarTarea)   
                    ]
                ),
                f.Row(
                    controls=[
                        todas, 
                        activas,
                        completadas,   
                    ]
                ),
                listaDeTareas,
                f.Row(
                    controls=[
                        f.Text("item activos restantes", size=10),
                        f.Button("Borrar Completados"),
                    ],
                ),
            ]
        ),
    )

if __name__ == "__main__":
    f.run(main)