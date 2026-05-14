#João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos. Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar. Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def ler_valor_e_porcentagem(mensagem):
    return float(int(mensagem).replace(",",".").strip())

def calculo_da_gorjeta(valor, porcentagem):
    
    if valor <= 0:
        raise ValueError ("Valor da conta deve ser maior que zero.")
    if porcentagem <= 0:
        raise ValueError ("Valor da porcentagem deve ser maior que zero.")
    
    gorjeta = valor * (porcentagem / 100)
    
    total = gorjeta + valor

    return gorjeta, total


try:
    valor = ler_valor_e_porcentagem("Digite o valor total da conta: ")

    porcentagem =  ler_valor_e_porcentagem("Digite a porcentagem da gorjeta: ")

    gorjeta, total = calculo_da_gorjeta(valor, porcentagem)

    print(f"\nValor da conta: R$ {valor:.2f}.")
    print(f"Valor dad gorjeta ({porcentagem:.0f}%): R$ {gorjeta:.2f}.")
    print(f"Total a pagar: R$ {total:.2f}.")

except ValueError as erro:
    print(f"Erro: {erro}.")

 #Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro. Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

def validar_cpf(cpf):

    cpf = cpf.strip()

    if not cpf.isdigit():
        raise ValueError ("Digite apenas números.")

    if len(cpf) != 11:
        raise ValueError ("O CPF deve conter 11 digitos.")
    
def ler_cpf():
    return input("Digite o seu CPF (apenas números): ").strip()
    
try:
    cpf = ler_cpf()

    validar_cpf(cpf)

    print (f"CPF {cpf} foi validado.")

except ValueError as erro:
    print (f"Erro: {erro}")

#Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas. Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

def contar_vogais(texto):

    vogais = "aáãâàeèéêiìíîoóòôõuùúû"

    contagem = {}

    for letra in texto.lower():
        if letra in vogais:
            contagem[letra] = (contagem.get(letra, 0) +1)
    return contagem

texto = input("Digite o texto para a contagem de vogais: ")

resultado = contar_vogais(texto)

total = sum(resultado.values())

print (f"\nNo texto, contem {total} vogais.")

for vogal, quantidade in resultado.items():
    print (f"{vogal}:{quantidade}")
    
#Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque. Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

import string

def encontrar_palavras_longas(texto):
    
    palavras = texto.split()

    palavras_longas = []

    for palavra in palavras:

        palavras_validadas = palavra.strip(string.punctuation)

        if palavras_validadas.isalpha() and len(palavras_validadas) > 10:
            palavras_longas.append(palavras_validadas)

    return palavras_longas

texto = input("Digite um texto para a contagem: ")

resultado = encontrar_palavras_longas(texto)    

if resultado:
    print("Palavras longas foram encontradas: ")
    for palavra in resultado:
        print(palavra)
else:
    print("Nenhuma palavra longa foi encontrada.")


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

#Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é. Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido. Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

import random

def advinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            entrada = input("Digite um número entre 1 e 100 para iniciar o jogo do número secreto: ").strip()

            if entrada == "":
                raise ValueError ("Você não digitou um número para jogar.\n")
            
            palpite = int(entrada)

            if not 1 <= palpite <= 100:
                raise ValueError ("Digite um número entre 1 e 100.\n")
            
            tentativas += 1

            if palpite > numero_secreto:
                print(f"O número secreto é menor que {palpite}!\n")
            elif palpite < numero_secreto:
                print(f"O número secreto é maior que {palpite}!\n")
            else:
                print(f"Parabéns, você acertou o número secreto em {tentativas}!")
                print(f"O número secreto era {numero_secreto}")
                break

        except ValueError as erro:
            print(f"Entrada inválida: {erro}\n")

advinhar_numero()

#Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros. Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:
#Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
#Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

def soma (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    if b == 0:
        raise ZeroDivisionError ("Não pode ser feita uma divisão por zero.\n")
    return a / b

def ler_numero(mensagem):
    while True:
        entrada = input(mensagem).strip()
    
        if entrada == "":
            print("Erro: Você precisa digitar um número.\n")
            continue

        try:
            return float(entrada)
        except ValueError:
            print("Erro: Digite apenas números\n")

def ler_operacao(mensagem):
    while True:
        operacao = input(mensagem).strip()

        if operacao == "":
            print("Erro: Você precisa escolher a operação.\n")
            continue
        
        if operacao in ("+", "-", "*", "/"):
            return operacao
        
        print("Erro: Operação inválida, escolha entre as opções: (+, -, *, /).\n")


def calcular ():
    try:
        numero1 = ler_numero("Digite o primeiro número: ")
        operacao = ler_operacao("Digite a operação desejada (+, -, *, /):")
        numero2 = ler_numero("Digite o segundo número: ")

        if operacao == "+":
            resultado = soma (numero1, numero2)
        elif operacao == "-":
            resultado = subtracao (numero1, numero2)
        elif operacao == "*":
            resultado = multiplicacao (numero1, numero2)
        else:
            resultado = divisao (numero1, numero2)
              
        print(f"O resultado de {numero1:0.2f} {operacao} {numero2:0.2f} é: {resultado:0.2f}")
            
    except ValueError as erro:
        print(f"Erro: {erro}")
    except ZeroDivisionError as erro:
        print(f"Erro: {erro}")

calcular()


#Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista. Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

def exibir_opcoes():
    print ("\n1. Adicionar tarefas.")
    print ("2. Visualizar Tarefas.")
    print ("3. Remover tarefas.")
    print ("4. Finalizar programa.\n")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa que deseja adicionar: ").strip()
    
    if tarefa:
        tarefas.append(tarefa)
    else:
        print ("Erro: A tarefa não pode estar vazia.")    

def visualizar_tarefas(tarefas):
    if tarefas:
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma terefa foi encontrada.")

def remover_tarefas(tarefas):
    visualizar_tarefas(tarefas)

    if tarefas:
        try:
            tarefa_para_excluir = int(input("Digite a tarefa que deseja remover: "))
            tarefas.pop(tarefa_para_excluir - 1)
            print("Tarefa removida com sucesso.")
        except:
            print("Opção inválida.")
    
def escolher_opcoes(tarefas):
    try:
        opcao_escolhida = int(input("Escolha uma das opções:").strip())

        if opcao_escolhida == 1:
            adicionar_tarefa(tarefas)
        elif opcao_escolhida == 2:
            visualizar_tarefas(tarefas)
        elif opcao_escolhida == 3:
            remover_tarefas(tarefas)
        elif opcao_escolhida == 4:
            return False
        else:
            print("Opção inválida.")
    except:
        print("Opção inválida.")

    return True

def main():
    tarefas = []

    while True:
        exibir_opcoes()
        continuar = escolher_opcoes(tarefas)

        if not continuar:
            print("Encerrando programa...")
            break

main()
        
