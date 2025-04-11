# Frameworks Python para desenvolvimento:
# Flask, Django, FastAPI, Flet, Kivy
# Neste exemplo, usaremos o Flet (frontend + backend em Python)

import flet as ft

def main(pagina: ft.Page):
    # Título principal da página
    titulo = ft.Text("Hashzap", size=30, weight="bold")

    # Título da janela de boas-vindas
    titulo_janela = ft.Text("Bem-vindo ao Hashzap")

    # Elementos do chat
    chat = ft.Column()  # Onde as mensagens vão aparecer
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=lambda e: enviar_mensagem(e))
    botao_enviar = ft.ElevatedButton("Enviar", on_click=lambda e: enviar_mensagem(e))
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])

    # Função que recebe mensagens pelo pubsub (websocket interno)
    def receber_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(receber_mensagem_tunel)

    # Enviar mensagem pelo pubsub
    def enviar_mensagem(evento):
        if campo_nome.value and campo_mensagem.value:
            mensagem = f"{campo_nome.value}: {campo_mensagem.value}"
            pagina.pubsub.send_all(mensagem)
            campo_mensagem.value = ""
            pagina.update()

    # Campo de nome e botão para entrar no chat
    campo_nome = ft.TextField(label="Digite o seu nome", on_submit=lambda e: entrar_chat(e))
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=lambda e: entrar_chat(e))

    # Janela de boas-vindas
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome,
        actions=[botao_entrar]
    )

    # Abrir o diálogo ao clicar em "Iniciar Chat"
    def abrir_dialog(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    # Entrar no chat e montar a interface principal
    def entrar_chat(evento):
        if campo_nome.value:
            pagina.pubsub.send_all(f"{campo_nome.value} entrou no chat")
            janela.open = False
            pagina.remove(titulo)
            pagina.remove(botao_iniciar)
            pagina.add(chat)
            pagina.add(linha_mensagem)
            pagina.update()

    # Botão inicial para abrir o chat
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

    # Adicionar os elementos iniciais na página
    pagina.add(titulo, botao_iniciar)

# Rodar a aplicação no navegador
ft.app(target=main, view=ft.WEB_BROWSER)
