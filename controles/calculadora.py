from dataclasses import field

import flet as f


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


@f.control
class CalculatorApp(f.Container):
    def init(self):
        self.width = 350
        self.bgcolor = f.Colors.BLACK
        self.border_radius = f.BorderRadius.all(20)
        self.padding = 20
        self.result = f.Text(value="0", color=f.Colors.WHITE, size=20)
        self.content = f.Column(
            controls=[
                f.Row(
                    controls=[self.result],
                    alignment=f.MainAxisAlignment.END,
                ),
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
                    ]
                ),
            ]
        )

"""
def main(page: f.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


f.run(main)
"""