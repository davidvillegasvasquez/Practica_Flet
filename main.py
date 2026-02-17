from controles.calculadora import CalculatorApp
from dataclasses import f

def main(pagina: f.Page):
    pagina.title = "Calc App"
    # create application instance
    calculadora1 = CalculatorApp()
    calculadora2 = CalculatorApp()

    # add application's root control to the page
    pagina.add(calculadora1, calculadora2)

f.run(main)