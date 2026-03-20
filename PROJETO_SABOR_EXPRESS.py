#POJETO SABOR EXPRESS

import os 

restaurantes = [{'nome': 'Merute', 'categoria': 'Arabe', 'ativo': False},
                {'nome': 'Botequin', 'categoria': 'Bar', 'ativo': True},
                {'nome': 'Pizza do seu Zé', 'categoria': 'Italiana', 'ativo': False}]

def exibir_nome_do_programa():
    ''' Exibe o nome do programa na tela, de forma mais estilizada.'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  \n""")

def exibir_opcoes():
    '''Exibe as opções que o usuário pode escolher para interagir com o programa.'''
    print ('1. Cadastrar restaurantes')
    print ('2. Listar restaurantes')
    print ('3. Alterar estado restaurantes')
    print ('4. Sair\n')

def finalizar_app():
    '''Finaliza o programa, exibindo uma mensagem de despedida para o usuário.'''
    exibir_subtitulos('Finalizar app, até mais...')

def voltar_ao_menu_principal():
    '''Essa função, proporciona ao usuário a possibilidade de voltar ao menu principal, após realizar uma ação solicitando qualquer tecla para isso.
    
    output's (SAIDAS):
    - Volta para o menu principal.
    '''
    input ('\nDigite uma tecla para voltar ao menu...')
    main()
 
def opcao_invalida():
    '''Caso o usuário escolhe uma opção que não se encontra dentro das opção, é informado que a opção é inválida, sugerindo que escolha uma opção válida, e é direcionado para o menu principal.
    output's (SAIDAS):
    - Volta para o menu principal.
    '''
    print ('Opção inválida. Por favor, escolha uma opção válida.\n')
    voltar_ao_menu_principal()

def exibir_subtitulos (texto):
    '''Essa função, facilita e deixa menos poluído o código, também para melhorar a vizualiação no terminal, pois deixa padronizado em limpar o histórico, sempre que um subtitulo for acionado, e acrescentar asteriscos a cima e a baixo dos subtitulos
    input's (ENTRADAS):
    - texto: string que representa o subtitulo a ser exibido.
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print (linha)
    print (texto)
    print (linha)
    print()

def cadastrar_novo_restaurante():

    ''' Essa função é responsável por cadastrar um novo restaurante.
    
    Input's (ENTRADAS):
    - nome_do_restaurante.
    - categoria.

    output's (SAÍDAS):
    - Adiciona um novo restaurente à lista de restaurantes.
    '''

    exibir_subtitulos ('Cadastro de novo restaurante')
    nome_do_restaurante = input ('Digite o nome do restaaurente: ')
    categoria = input (f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print (f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista todos os restaurantes cadastrados, informando o nome, categoria e se o restaurante está ou ão ativo
    output's (SAIDAS):
    - Exibe a lista de restaurantes na tela.
    '''
    exibir_subtitulos ('Lista de restaurantes cadastrados:')

    print (f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo = 'Ativado' if restaurante ['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Permite alterar o estado do restaurante entre ativo e desativo.
    output's (SAIDAS):
    - Exibe uma mensagem informando se o restaurante foi ativado ou desativado com sucesso.
    - Caso o restaurante não seja encontrado, exibe uma mensagem informando que o restaurante não foi encontrado.
    '''
    exibir_subtitulos ('Alternando estado do restaurante')
    nome_restaurante = input ('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante ['ativo']
            mensagem = (f'O restaurante {nome_restaurante} foi ativado com sucesso!') if restaurante ['ativo'] else (f'O restaurente {nome_restaurante} foi desativado com sucesso!')
            print (mensagem)

    if not restaurante_encontrado:
        print (f'O restaurente {nome_restaurante} não foi encontrado. Por favor, verifique e tente novamente')
            
    


    voltar_ao_menu_principal()

def escolher_opcoes():
    '''Solicitar e executar a opção escolhida pelo usuário.
    Output's (SAIDAS):
    - Executa e função correspondente a solicitada pelo usuário.
    '''
    try:
        opcao_escolhida = int(input ('Escolha uma opção: '))
    # opcao_escolhida = int (opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

def main():
    '''A função principal do programa, a primeira a ser exibida'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

    
if __name__ == '__main__':
    main()