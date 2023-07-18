#configurcao da pagina
import flet as ft

def main(page:ft.Page):
    # Titulo da pagina
    page.title = "Aplicação teste"
    # tema da pagina
    page.theme_mode = ft.ThemeMode.DARK
    page.update()



#tema da pagina


ft.app(target=main, view=ft.WEB_BROWSER)