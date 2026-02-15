import flet as f

def main(pagina: f.Page):
    pagina.title = "App Calculadora"
    resultado = f.Text(value="0")

    pagina.add(
        resultado,
        f.Button("AC"),
        f.Button("+/-"),
        f.Button("%"),
        f.Button("/"),
        f.Button("7"),
        f.Button("8"),
        f.Button("9"),
        f.Button("*"),
        f.Button("4"),
        f.Button("5"),
        f.Button("6"),
        f.Button("-"),
        f.Button("1"),
        f.Button("2"),
        f.Button("3"),
        f.Button("+"),
        f.Button("0"),
        f.Button("."),
        f.Button("="),
    )


if __name__ == "__main__":
    f.run(main)
