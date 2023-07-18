import flet as ft
def main(page): #Aqui, está sendo definida uma função chamada main,
                # que recebe um argumento chamado page.

    def login(e):                                    #Neste trecho, está sendo definida uma função chamada login,
                                                # que recebe um argumento e, um evento relacionado ao botão
        if not  entrada_nome.value:
            entrada_nome.error_text = "Por favor preencha seu nome"
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Campo de senha obrigatório"
            page.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")


            page.clean() #função para limpar a pagina
            page.add(ft.Text(f"Olá, {nome}\nSeja bem vindo a nossa aplicação"))
            pass

    entrada_nome = ft.TextField(label="Digite seu nome") #Aqui, estão sendo criados dois campos de entrada de
                                                         # texto usando a função TextField
    entrada_senha = ft.TextField(label="Digite sua senha")
    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Clique em mim", on_click=login)
    )
    pass

ft.app(target=main)