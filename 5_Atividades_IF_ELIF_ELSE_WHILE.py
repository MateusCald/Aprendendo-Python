#LOOPS - IF, ELIF, ELSE E WHILE.

1#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
macas = int(input('Digite o número de maças vendidas: '))
bananas = int(input('Digite o número de bananas vendidas: '))
diferenca = abs(macas - bananas)

if macas > bananas:
    print (f'As maças tiveram mais vendas, sendo vendidas {macas}, com diferença de {diferenca} unidade(s) a mais que a banana ({bananas} unidade(s)).')
elif bananas > macas:
    print (f'As banas tiveram mais vendas, sendo vendidas {bananas}, com diferença de {diferenca} unidade(s) a mais que a maça ({macas} unidade(s)).')
else:
    print (f'Ambos produtos tiveram a mesma quantidade de vendas, (Bananas {bananas} e Maças {macas}).')


2#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
atividade_A = int(input('Informe o número de dias utilizados para finalizar a atividade A: '))
atividade_B = int(input('Informe o número de dias utilizados para finalizar a atividade B: '))
atividade_C = int(input('Informe o número de dias utilizados para finalizar a atividade C: '))

if atividade_A < 0 or atividade_B < 0 or atividade_C < 0:
    print ('Erro: Os dias informados não devem conter numeração negativa')
else:
    tempo_total = atividade_A + atividade_B + atividade_C
    print (f'O tempo total utilizado para finalizar as atividades foram de: {tempo_total} dias')

3#Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura = float(input('Digite a temperatura atual: '))

if temperatura > 25:
    print ('Alerta! Temperatura a cima do limite seguro')
else:
    print (f'A temperatuda é de {temperatura} graus, está dentre do limite de segurança')

4#O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print (f'Seu IMC é de: {IMC:.2f}, se encontra abaixo do peso.')
elif 18.5 <= IMC < 25:
    print (f'Seu IMC é de: {IMC:.2f}, se encontra em normalidade.')
else:
    print (f'Seu IMC é de: {IMC:.2f}, se encontra acima do peso.')

5#Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
limite = 3000.00
despesa_mensal = float(input('Digite a despesa total do mês: R$ '))

diferenca = despesa_mensal - limite

if diferenca > 0:
    print (f'Atenção! Você ultrapassou o limite orçado em: R$ {diferenca:.2f}')
elif diferenca < 0:
    print (f'Você ainda tem: R$ {abs(diferenca):.2f} disponíveis do orçamento')
else:
    print (f'Você utilizou exatamente o valor do orçamento estipulado: R$ {limite}')

6#O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado. 
hora_atual = input ('Digite a hora atual (HH:MM): ')

hora, minuto = hora_atual.split(':')
hora = int(hora)
minuto = int(minuto)

total_minutos = hora * 60 + minuto

inicio = 8 * 60
fim = 18 * 60

if inicio <= total_minutos < fim:
    print ('Acesso permitido.')
else:
    print ('Acesso negado.')

7#Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
#Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
#Média < 5: Reprovado
primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))
terceira_nota = float(input('Digite sua terceira nota: '))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print (f'Sua média é {media:.1f}, Aprovado')
elif 5 <= media < 7:
    print (f'Sua média é {media:.1f}. Recuperação')
else:
    print (f'Sua média é {media:.1f}, Reprovado')

#8Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
#Até 100 km: R$ 10,00
#Entre 100 km e 200 km: R$ 20,00
#Acima de 200 km: R$ 30,00
distancia_percorrida = int(input('Digite a distância percorrida em KM: '))

distancia_100 = 10.00
distancia_100_a_200 = 20.00
distancia_200_mais = 30.00

if distancia_percorrida <= 100:
    print (f'A distância percorrida foi de {distancia_percorrida} Km, o valor do pedágio é de: R$ {distancia_100}')
elif 100 < distancia_percorrida <= 200:
    print (f'A distância percorrida foi de {distancia_percorrida} Km, o valor do pedágio é de: R$ {distancia_100_a_200}')
else:
    print (f'A distância percorrida foi de {distancia_percorrida} Km, o valor do pedágio é de: R$ {distancia_200_mais}')

9#Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print (f'O número {numero}, é par')
else:
    print (f'O número {numero}, é impar')

10#Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
#O valor da renda mensal precisa ser maior que R$ 2.000,00.
#O valor da parcela não pode ultrapassar 30% da renda.
#Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.
renda = float(input('Digite o valor mensal de sua renda: '))
parcela_desejada = float(input('Digite o valorda parcela desejada: '))

if renda <= 0 or parcela_desejada <=0:
    print ('Valores inválidos.')
elif renda < 2000:
    print ('Empréstimo negado: Renda insuficiente.')
else:
    limite_da_parcela = renda * 0.3

    if parcela_desejada > limite_da_parcela:
        print ('Empréstimo negado: Valor da parcela superior a 30% da renda.')
    else:
        print ('Empréstimo aprovado!')

11#Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.
clientes = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

for cliente in clientes:
    print (cliente)

12#Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" 5 vezes
for i in range (5):
    print ('Bem-vindo ao Buscante')

13#Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
valores = [10, 20, 30, 40, 50]

soma = 0 

for valor in valores:
    soma += valor

print (f'A soma total das receitas é: {soma}')

14#Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".
projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

for projeto in projetos:
    if projetos is None:
        print ('Projeto ausente')
    else:
        print (projeto)

15#Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.
livros = ['1984', 'Dom Casmurro', 'O Pequeno Príncipe', 'O Hobbit', 'Orgulho e Preconceito']

for livro in livros:
    if livro == 'O Hobbit':
        print (f'Livro encontrado: {livro}')
        break

16#Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
estoque_de_livros = 5 

while estoque_de_livros > 0:
    estoque_de_livros -= 1
    print (f'Venda realizada! Estoque restante: {estoque_de_livros}.')

print ('Estoque esgotado.')

17#Crie um programa que utilize um laço for para exibir as seguintes mensagens:
#Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
#Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
#Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".

for segundos in range (10, 0, -1):
    if segundos % 2 == 0:
        print (f'Falta apenas {segundos} segundos - Não perca essa oportunidade!')
    else:
        print (f'A contagem continua: {segundos} segundos restantes.')
print ('Aproveite a promoção agora!')

18#Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato: "Livro disponível: ".
livros = [
    {'nome': '1984', 'estoque': 5},
    {'nome': 'Dom Casmurro', 'estoque': 0},
    {'nome': 'O Pequeno Príncipe', 'estoque': 3},
    {'nome': 'O Hobbit', 'estoque': 0},
    {'nome': 'Orgulho e Preconceito', 'estoque': 2}
]  

for livro in livros:
    if livro ['estoque'] > 0:
        print (f'Livro disponível: {livro["nome"]}.')  
        break

19#João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:
#O nome de usuário deve ter pelo menos 5 caracteres.
#A senha deve ter pelo menos 8 caracteres.
#João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

while True:

    usuario = input('Digite seu nome de usuário: ')
    if len (usuario) < 5:
        print ('O nome do usuário deve conter ao menos 5 caracteres.')
        continue

    senha = input('Digite sua senha: ')
    if len (senha) < 8:
        print ('A senha deve conter ao menos 8 caracteres.')
        continue
    
    print('Cadastro realizado com sucesso!')
    break