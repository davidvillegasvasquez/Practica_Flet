import flet as f


def main(pagina: f.Page):
    pagina.title = "Calc App"
    result = f.Text(value="0")

    pagina.add(
        f.Row(controls=[result]),
        f.Row(
            controls=[
                f.Button("AC"),
                f.Button("+/-"),
                f.Button("%"),
                f.Button("/"),
            ]
        ),
        f.Row(
            controls=[
                f.Button("7"),
                f.Button("8"),
                f.Button("9"),
                f.Button("*"),
            ]
        ),
        f.Row(
            controls=[
                f.Button("4"),
                f.Button("5"),
                f.Button("6"),
                f.Button("-"),
            ]
        ),
        f.Row(
            controls=[
                f.Button("1"),
                f.Button("2"),
                f.Button("3"),
                f.Button("+"),
            ]
        ),
        f.Row(
            controls=[
                f.Button("0"),
                f.Button("."),
                f.Button("="),
            ]
        ),
    )


if __name__ == "__main__":
    f.run(main)