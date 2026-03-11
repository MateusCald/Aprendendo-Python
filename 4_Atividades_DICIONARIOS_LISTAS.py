#DICIONARIOS E LISTAS.

1#Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
informacoes_pessoais = {'Nome': 'Mateus', 'Idade': 26, 'Cidade': 'São Paulo'}

2#Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
informacoes_pessoais ['Idade'] = 27

#Adicione um campo de profissão para essa pessoa;
informacoes_pessoais ['Profissão'] = 'Programador'

#Remova um item do dicionário.
del informacoes_pessoais ['Cidade']

3#Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrados = {x: x**3 for x in range (1, 6)}
print (numeros_quadrados)

4#Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dicionario_para_pesquisar = {'Chave1': 'Valor1', 'Chave2': 'Valor2', 'Chave3': 'Valor3'}

pesquisa_usuario = input ('Digite a chave que deseja pesquisar: ')

if pesquisa_usuario in dicionario_para_pesquisar:
    print (f'A chave {pesquisa_usuario} existe no dicionário, o valor associado a ela é: {dicionario_para_pesquisar[pesquisa_usuario]}')
else:
    print (f'A chave {pesquisa_usuario} não existe no dicionário, por favor, verifique e tente novamente.')

5#Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase_usuario = input('Digite uma frase para contar a frequência de cada palavra: ')
frequencia_palavras = {}
palavras = frase_usuario.split()

for palavra in palavras:
    frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1
    print (f'A frequência de cada palavra na frase é: {frequencia_palavras}')
