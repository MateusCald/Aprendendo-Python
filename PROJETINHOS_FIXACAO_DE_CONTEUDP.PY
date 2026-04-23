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
    
