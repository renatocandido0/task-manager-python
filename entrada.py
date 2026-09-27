def obter_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Opção inválida. Digite um número.")

def obter_texto(mensagem):
    while True:
        texto = input(mensagem)
        if texto.strip() == "":
            print("Você não digitou nada")
        else:
            return texto.strip()
