from dataclasses import field

import flet as f


def main(pagina: f.Page):
    pagina.title = "Calc App"
    result = f.Text(value="0", color=f.Colors.WHITE, size=20)

    @f.control
    class CalcButton(f.Button):
        expand: int = field(default_factory=lambda: 1)

    @f.control
    class DigitButton(CalcButton):
        bgcolor: f.Colors = f.Colors.WHITE_24
        color: f.Colors = f.Colors.WHITE

    @f.control
    class ActionButton(CalcButton):
        bgcolor: f.Colors = f.Colors.ORANGE
        color: f.Colors = f.Colors.WHITE

    @f.control
    class ExtraActionButton(CalcButton):
        bgcolor: f.Colors = f.Colors.BLUE_GREY_100
        color: f.Colors = f.Colors.BLACK

    pagina.add(
        f.Container(
            width=350,
            bgcolor=f.Colors.BLACK,
            border_radius=f.BorderRadius.all(20),
            padding=20,
            content=f.Column(
                controls=[
                    f.Row(controls=[result], alignment=f.MainAxisAlignment.END),
                    f.Row(
                        controls=[
                            ExtraActionButton(content="AC"),
                            ExtraActionButton(content="+/-"),
                            ExtraActionButton(content="%"),
                            ActionButton(content="/"),
                        ]
                    ),
                    f.Row(
                        controls=[
                            DigitButton(content="7"),
                            DigitButton(content="8"),
                            DigitButton(content="9"),
                            ActionButton(content="*"),
                        ]
                    ),
                    f.Row(
                        controls=[
                            DigitButton(content="4"),
                            DigitButton(content="5"),
                            DigitButton(content="6"),
                            ActionButton(content="-"),
                        ]
                    ),
                    f.Row(
                        controls=[
                            DigitButton(content="1"),
                            DigitButton(content="2"),
                            DigitButton(content="3"),
                            ActionButton(content="+"),
                        ]
                    ),
                    f.Row(
                        controls=[
                            DigitButton(content="0", expand=2),
                            DigitButton(content="."),
                            ActionButton(content="="),
                        ],
                    ),
                ] #Cierre del controls de la primera columna del container
            ), #Cierre del content del container
        ) #Cierre del container
    ) #Cierre del add


if __name__ == "__main__":
    f.run(main)