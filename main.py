import flet as ft

def main(page: ft.Page):
    page.title = "Mi App Flet en Codespaces"
    page.add(ft.Text("Hola, mundo!"))

ft.app(target=main, view=ft.AppView.WEB_BROWSER) # Ejecutar en navegador
