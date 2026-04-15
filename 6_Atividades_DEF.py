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



#4Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
#Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:




#5Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

#Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.



#Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário. Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().



#Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço. Crie um programa que junte as listas e exiba o resultado no formato produto: preço



#Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números. Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.


#Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.


