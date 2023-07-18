import flet as ft
#construcao de uma lista de items no browser


def main(page: ft.Page):
    for i in range(500):
        page.controls.append(ft.Text(f"Estamos na linha {i}"))

    page.scroll = "always"
    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)