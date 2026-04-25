#João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos. Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar. Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def calculo_da_gorjeta(valor, porcentagem):

    if valor <= 0:
        raise ValueError ("Valor da conta inválido.")
    if porcentagem <= 0:
        raise ValueError ("Valor da porcemtagem inválido.")
    gorjeta = valor * (porcentagem / 100)
    total = gorjeta + valor

    return gorjeta, total

try:
    valor = float(input("Digite o valor total da conta: ").replace(",",".").strip())

    porcentagem = float(input("Digite a porcentagem de gorjeta: ").strip())

    gorjeta, total = calculo_da_gorjeta(valor, porcentagem)

    print(f"Valor do pedido: R$ {valor:.2f}")
    print(f"Gorjeta ('{porcentagem:.0f}%'): R$ {gorjeta}")
    print(f"Total a pagar: R$ {total:.2f}")

except ValueError as erro:
    print (f"Erro: {erro}")

 #Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro. Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

def contar_digitos_do_cpf (cpf):
    cpf = cpf.strip()
    
    if not cpf.isdigit():
        raise ValueError ("Por gentileza, digite apenas os números de seu CPF: ")
    
    if len(cpf) != 11:
        raise ValueError ("Por gentileza, digite apenas os 11 digitos numéricos de seu CPF: ")
    
    return "CPF válido."

try:
    cpf = input("Digite o seu CPF: ")

    contagem = contar_digitos_do_cpf(cpf)

    print(contagem)

except ValueError as erro:
    print(f"Erro: {erro}.")

#Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas. Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

def contagem_de_vogais(texto):
    if not isinstance (texto, str):
        raise ValueError ("Por gentileza, utilize apenas letras:")
    
    vogais = "aàáâãeéèêiíìîoóòôõuúùû"
    quantidade = 0
    
    for letra in texto.lower():
        if letra in vogais:
            quantidade += 1
    
    return quantidade

texto = input("Digite um texto para a contagem de vogais: ")

print(f"No texto informado contém {contagem_de_vogais(texto)} vogais!")
    
#Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque. Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

def encontrar_palavras_longas(texto):
    if not isinstance (texto, str):
        raise TypeError ("Por gentileza, utilizar palavras.")
    
    palavras = texto.strip().split()
    palavras_longas = []

    for palavra in palavras:
        if len(palavra) > 10:
            palavras_longas.append(palavra)

    return palavras_longas

texto = input("Digite um texto: ")

resultado = encontrar_palavras_longas(texto)

if resultado:
    print ("Palavras longas foram encontradas:")
    for palavra in resultado:
        print(palavra)

else:
    print("Nenhuma palavra longa foi encontrada;")

#Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais. Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

import random

def gerar_senha_aleatoria():
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    caracteres_especiais = "!@#$%&*"

    senha = []

    senha.append(random.choise(letras_maiusculas))
    senha.append(random.choise(letras_minusculas))
    senha.append(random.choise(numeros))
    senha.append(random.choise(caracteres_especiais))

    todos = letras_minusculas + letras_minusculas + numeros + caracteres_especiais

    senha.extend(random.choices(todos, k=8))

    random.shuffle(senha)

    return "".join(senha)

print(gerar_senha_aleatoria())

#Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.
#Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:
#Pedra ganha de Tesoura (Pedra quebra Tesoura);
#Tesoura ganha de Papel (Tesoura corta Papel);
#Papel ganha de Pedra (Papel cobre Pedra);
#Se ambos escolherem a mesma opção, é um empate.

import random

def pedra_papel_tesoura(escolha):
    escolha = escolha.lower().strip()

    if not escolha:
        raise ValueError ("Sua jogada esta vazia.")
    
    opcoes = [
        "tesoura",
        "pedra",
        "papel"
    ]

    if escolha not in opcoes:
        raise ValueError ("Sua escolha não está dentro das opções (pedra, papel e tesoura).")
    
    escolha_computador = random.choice(opcoes)

    vitorias = {
        "pedra":"tesoura",
        "papel":"pedra",
        "tesoura":"papel"
    }

    if escolha == escolha_computador:
        resultado = "Empate!"
    elif vitorias[escolha] == escolha_computador:
        resultado = "Você venceu!"
    else:
        resultado = "Você perdeu!"
    
    return escolha_computador, resultado

try:
    escolha_jogador = input("Escolha entre pedra, papel e tesoura, para jogar com o computador:")

    computador, resultado = pedra_papel_tesoura(escolha_jogador)
    
    print(f"O computador escolheu {computador}!")    
    print(resultado)
    
except ValueError as erro:
    print(erro) 
