#FUNÇÕES - DEF.

#1 Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

def calcular_idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento
    

try:
    nascimento = input("Digite o ano de seu nascimento: ")
    atual = input("Digite o ano atual: ")

    if not (nascimento.isdigit() and atual.isdigit()):
        raise ValueError ("Digite apenas números: ")
    
    if len(nascimento) != 4 or len(atual) != 4:
        raise ValueError ("Por gentileza, informe os anos utilizando 4 digitos (Ex: 1999): ")
    

    nascimento = int(nascimento)
    atual = int(atual)

    if nascimento > atual:
        raise ValueError ("O ano de nascimento não pode ser maior que o ano atual.")

    idade = calcular_idade(atual, nascimento)

    print (f"Sua idade é de {idade} anos")

except ValueError as erro:
    print (erro)



#2 Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
#Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def contar_caracter(texto):
    return len(texto.strip().replace(" ",""))

entrada = input("Digite o texto para contagem de caracter: ")

if entrada.strip() == "":
    print ("Você não digitou nenhum texto.")
else:
    quantidade = contar_caracter(entrada)
    print(f"A quantidade de caracteres do texto informado é de: {quantidade} caracteres.")


#3Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:
#Se for antes das 12h, exibir "Bom dia";
#Entre 12h e 18h, exibir "Boa tarde";
#Após 18h, exibir "Boa noite".z

def saudacao_personalizada(hora, minuto):
    if not  (0 <= hora <= 23 and 0 <= minuto <= 59):
        return ("Horário inválido, digite novamente: ")
        
    if hora < 12:
        return ("Bom dia!")
    elif hora < 18:
        return ("Boa tarde!")
    else:
        return ("Boa noite!")


try:
    horario = input("Digite a hora atual (HH:MM): ").strip()

    hora, minuto = horario.split(":")

    if not horario:
        raise ValueError
        
    hora = int(hora)
    minuto = int(minuto)

    print (f"Horário formatado: {hora:02d}:{minuto:02d}")
    print (saudacao_personalizada(hora, minuto))
except ValueError:
    print("Formato incorreto, siga conforme solicitado (Ex 09:30): ")


#4Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
#Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

def converter_telefones(lista):
    telefones_convertidos = []
    for telefone in lista:
        try:
            telefones_convertidos.append(int(telefone))
        except ValueError:
            raise ValueError (f"Erro: O número de telefone '{telefone}' não é válido.")
    return telefones_convertidos

def validar_conversao(entrada):
    if not entrada:
        raise ValueError("Erro: A lista de telefones está vazia.")
    for telefone in entrada:
        if not isinstance(telefone, int):
            raise ValueError("Erro na conversão.")
    return "Todos os números foram convertidos corretamente."

entrada = input("Digite os números de telefone separados por vírgula: ").split(",")

try:
    conversao = converter_telefones(entrada)
    print(validar_conversao(conversao))
except ValueError as erro:
    print(erro)


#5Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

#Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

def total_vendas(vendas):
    if not vendas:
        raise ValueError("Nenhum valor informado.")
    
    total = 0

    for venda in vendas:
        try:
            total += float(venda)
        except ValueError:
            raise ValueError (f"O valor '{venda}' não é um número válido.")
    return (total)

try:
    vendas = input("Digite os valores das vendas separadas por espaço:").strip().replace(",",".").split()

    soma = total_vendas(vendas)

    print(f"O valor total das vendas é de: R$ {soma:.2f}")
except ValueError as erro:
    print(erro)


#Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário. Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

numeros = list(map(int, input("Digite os numeros separados por espaço: ").split()))

pares = list(filter(lambda x: x % 2 == 0, numeros))

print (f"Os números pares são: {pares}")


#Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço. Crie um programa que junte as listas e exiba o resultado no formato produto: preço

produtos = input("Digite os produtos separados por espaço: ").split()

precos =  map(float,input("Digite os precos separados por espaço: ").replace(",",".").split())

precos_dos_produtos = list(zip(produtos, precos))

for produto, preco in precos_dos_produtos:
    print(f"{produto.strip()}:{preco:.2f}")


#Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números. Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

operacoes = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Erro: Não pode ser feito divisão por 0!"
}

x = float(input("Digite o primeiro número para operação: ").replace(",","."))

y = float(input("Digite o segundo número para operação: ").replace(",","."))

operacao = input("Escolha a operação que deseja fazer (+, -, *, /): ")

if operacao in operacoes:
    print (f"O resultado é: {operacoes[operacao](x, y):.2f}:")
else:
    print("Operação inválida!")

#Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

def porcentagem_de_desconto(porcentagem):

    def valor_da_compra(valor):
        return (valor-(valor*(porcentagem/100)))
    return valor_da_compra

porcentagem = int(input("Digite a porcentagem que será aplicada ao desconto:"))

valor = int(input("Digite o valor total da compra: "))

calcular_preco_final = porcentagem_de_desconto (porcentagem)

print (f"Preço final com desconto: {calcular_preco_final(valor):.2f}")

#Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

#Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

def soma_recursiva(n):
    if n == 1:
        return n
    return n + soma_recursiva (n -1)

try:
    numero = int(input("Digite um número:"))

    if numero > 0:
        print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}")
    else:
        print("Digite um número inteiro positivo:")

except ValueError:
    print ("Utilize apenas números:")
    
