from dataclasses import dataclass
import flet as f

@dataclass
class Tarea:  # noqa: B903
    texto: str

@f.control
class LineaDeTarea():
    def __init__(self, tarea: Tarea):
        super().__init__()
        self.tarea = tarea
        self.controls = [
            f.Row(
                tight=True,
                spacing=5,
                controls=[
                    #f.CheckBox(),
                    f.Text(self.tarea.texto, selectable=True),
                    #f.IconoLapicero(),
                    #f.IconoPapelera,
                ],
            ),
        ]

def main(pagina: f.Page):
    pagina.title = "Para Hacer"
    encabezado = f.Text(value="Tareas", color=f.Colors.BLACK, size=40)
    nuevaTarea = f.TextField()
    listaDeTareas = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    def clickEnMenuTodasActivasCompletadas(eventoMenuTodActiComple):
        # eventoMenuTodActiComple.control es el texto que fue clickeado
        eventoMenuTodActiComple.control.color = "blue"
        eventoMenuTodActiComple.control.weight = "bold"
        eventoMenuTodActiComple.control.decoration = f.TextDecoration.UNDERLINE
        eventoMenuTodActiComple.control.update() # Actualiza el elemento en pantalla

    # Crear los textos con propiedades iniciales
    todas = f.Text("Todas", size=20, color="black")

    activas = f.Text("Activas", size=20, color="black")#, on_click=clickEnMenuTodasActivasCompletadas)

    completadas = f.Text("Completadas", size=20, color="black")#, on_click=clickEnMenuTodasActivasCompletadas)

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
                    ],
                ),
                ft.Container(
                    content=listaDeTareas,
                    expand=True,
                ),   
                f.Row(
                    controls=[
                        f.Text("item activos restantes", size=10),
                        f.Button("Borrar Completados"),
                    ],
                ),
            ]
        ),
    )

f.run(main)