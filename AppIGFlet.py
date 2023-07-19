from flet import *


def main(page:Page):

    page.appbar = AppBar(
        leading=Icon(icons.CODE),
        leading_width=40,
        bgcolor="#003377",
        title=Text("Minha Loja"),
        actions=[
            IconButton(icons.WB_SUNNY),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="logar"),
                    PopupMenuItem(text="Inscrever-se")
                ]

            )
        ]

    )

    page.add(Text("Corpo!"))


app(target=main)