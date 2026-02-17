from controles.calculadora import CalculatorApp
import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Calc App"
    # create application instance
    calculadora1 = CalculatorApp()
    calculadora2 = CalculatorApp()

    # add application's root control to the page
    pagina.add(calculadora1, calculadora2)

ft.run(main)