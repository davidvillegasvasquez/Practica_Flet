import flet as f

# Use of GestureDetector with on_pan_update event for dragging tarjeta
# Absolute positioning of controls within stack

def main(pagina: f.Page):
    def arrastrar(evento: f.DragUpdateEvent):
        evento.control.top = max(0, evento.control.top + evento.delta_y)
        evento.control.left = max(0, evento.control.left + evento.delta_x)
        evento.control.update()

    tarjeta = f.GestureDetector(
       mouse_cursor=f.MouseCursor.MOVE,
       drag_interval=5,
       on_pan_update=arrastrar,
       left=0,
       top=0,
       content=f.Container(bgcolor=f.Colors.GREEN, width=70, height=100),
    )

    pagina.add(f.Stack(controls=[tarjeta], width=1000, height=500))

f.run(main)