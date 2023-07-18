#
import flet as ft
#defifindo a função inicial
def main(page: ft.Page):
    ola = ft.Text(value="Ola, Mundo!", size=30) #a variavel "ola" vai  recebr o comando de texto + o value (conteudo que sera exibido)
    page.controls.append(ola) #peguei a pagina, os controles e adicionei (append) o conteudo dentro, no caso a variavel ola
    page.update() #funcao que vai atualizar a sua pagina com os conteudos que voce adicionou


#o parametro target vai receber a funcao main, que esta rodando a aplicação
ft.app(target=main)