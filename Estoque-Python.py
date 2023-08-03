listaProdutos = []
#----- COMEÇO cadastrarProduto -----#
def cadastrarProduto (Código):
    print('Você Selecionou a Opção de Cadastrar Produto')
    print('Código do Produto {}'.format(Código))
    nome = input('Por favor entre com o NOME do produto: ')
    fabricante = input('Por favor entre com o FABRICANTE do produto: ')
    valor = int(input('Por favor entre com o VALOR do produto: '))
    dicionarioProduto = {'Código' : Código,
                          'nome' : nome,
                          'fabricante' :fabricante,
                          'valor' : valor}
    listaProdutos.append(dicionarioProduto.copy())
#----- FIM cadastrarProduto -----#

#----- COMEÇO consultarProduto -----#
def consultarProduto ():
    while True:
        try:
            print('Você Selecionou a Opção de Consultar Produto')
            opConsultar = int(input('Escolhe a opção desejada: \n'
                                    '1-Consultar Todos os Produtos\n'
                                    '2-Consultar Produtos por Código\n'
                                    '3-Consultar Produtos por Fabricante\n'
                                    '4- Retornar\n'
                                    '>>'))
            if opConsultar == 1:
                print('-'*20)
                for produto in listaProdutos:
                    for key, value in produto.items():
                        print('{} : {}'.format(key,value))
            elif opConsultar == 2:
                codig= int(input('Digite o CÓDIGO do Produto: '))
                for produto in listaProdutos:
                    if(produto['Código'] == codig):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 3:
                print('')
                codig = input('Digite o FABRICANTE do Produto: ')
                for produto in listaProdutos:
                    if (produto['fabricante'] == codig):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4:
                return
            else:
                print('Opção inválida')
                continue
        except ValueError:
            print('Digite apenas números inteiros')
#----- FIM consultarProduto -----#

#----- COMEÇO removerProduto -----#
def removerProduto ():
    print('Você Selecionou a Opção de Remover Produto')
    codig = int(input('Digite o código do Produto a ser removido: '))
    for produto in listaProdutos:
        if (produto['Código'] == codig):
            listaProdutos.remove(produto)
#----- FIM removerProduto -----#

#----- COMEÇO da MAIN -----#
print('Bem Vindo ao Controle de Estoque de Mercearia do Ricardo Douglas da Silva Mariz')
contadordeprodutos = 0
while True:
    try:
        opcao =int(input('Escolha a opção desejada:\n'
                         '1-Cadastrar Produto\n'
                         '2-Consultar Produto(s)\n'
                         '3-Remover Produto\n'
                         '4-Sair\n'
                         '>>'))
        if opcao == 1:
            contadordeprodutos = contadordeprodutos +1
            cadastrarProduto(contadordeprodutos)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Finalizando programa')
            break
        else:
            print('Opção inválida')
            continue
    except ValueError:
        print('Digite apenas números inteiros')
#----- FIM da MAIN -----#

