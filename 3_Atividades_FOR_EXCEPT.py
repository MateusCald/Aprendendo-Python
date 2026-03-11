#LISTAS, FOR, EXCEPT.

1#Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['Mateus', 'Gabriel', 'Anna', 'Ninguem']
lista_anos = [1999, 2026]

2#Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
numero = [1,2,3,4]
for i in numero:
    print(i)

3#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0

for i in range (1, 11, 2):
    soma_impares += i

print (f'A soma dos números impares de 1 a 10 é: {soma_impares}')

4#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range (10, 0, -1):
    print (i)

5#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número para ver na tabuada de 1 a 10: '))

for i in range (1, 11):
    resultado = numero * i
    print (f'{numero} x {i} = {resultado}')

6#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
numeros = [1,2,3,4,5]

soma_numeros = 0

try:
    for i in numeros:
        soma_numeros += i
    print (f'A soma dos números é: {soma_numeros}')
except TypeError:
    print ('Erro: A lista informada contém um elemento não identificado como número.')

7#Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_numeros = [1,2,3,4,5]
soma_valores = 0

try:
    for i in lista_numeros:
        soma_valores += i
    media = soma_valores / len(lista_numeros)
    print (f'A média dos valores é: {media}')
except ZeroDivisionError:
    print ('Erro: A lista está vazia, não é possivél calcular a média.')
except Exception as e:
    print (f'Erro: {e}')