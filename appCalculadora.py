from controles.calculadora import AppCalculadora 
import flet as f #Debo importar flet así AppCalculadora lo haya hecho en su módulo.

def main(pagina: f.Page):
    pagina.title = "App de Calculadora"
    # create application instance
    calculadora1 = AppCalculadora()
    calculadora2 = AppCalculadora()

    #Si agregamos los controles de la forma más simple, se colocaran una debajo de la otra en la pagina, como si estuvieran dentro de una columna:
    pagina.add(calculadora1, calculadora2)

    #Si queremos mostrar una al lado de otra, debemos colocarlo dentro de un control fila.
    #Recuerde que el primer parámetro posicional tiene el nombre "controls", y es una lista - f.Row(controls=[ctl1,ctl2,...], de modo que podemos prescindir de su nombre:
    pagina.add(f.Row([calculadora1, calculadora2]))
    
f.run(main)