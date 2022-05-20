import os

arquivos = os.listdir()

excecao = ['masterformula.py', '.git', '.gitignore', 'resultados.txt', 'pedidos', 'master.bat' ]

for exc in excecao:
    if exc in excecao:
        arquivos.remove(exc)


def master_formula(file: str):
    produtos = []
    pedido = ''
    identificador = ''
    layout = ''
    cnpj = ''
    data = ''
    dia = ''
    mes = ''
    ano = ''
    qtde_itens = ''
    qtde_total_unid = ''
    cod_cli = ''
    with open(file, mode='r', encoding='utf-8') as arquivo:
        linha = arquivo.readline()
        while linha:
            if linha.startswith('03'):
                produtos.append(linha[3:16])

            if linha.startswith('01'):
                identificador = linha[:2]
                layout = linha[2:6]
                cnpj = linha[8:22]
                cod_cli = linha[23:31]
                pedido = linha[31:40]
                data = linha[42:48]

            if linha.startswith('09'):
                qtde_itens = int(linha[3:6])
                qtde_total_unid = int(linha[7:15])

            linha = arquivo.readline()

        print('-' * 48)
        print(f'Pedido {pedido} Arquivo: {file}')
        print('-' * 48)
        print(f'Identificador = {identificador} Layout = {layout}')
        print(f'Código Cliente = {cod_cli} CNPJ = {cnpj}')
        print(f'Data = {data}')
        print('')
        for produto in produtos:
            print(f'EAN = {produto}')
        print(f'Qtde itens = {qtde_itens} | Qtde Tot. UN = {qtde_total_unid}')
        print(f'')
        # return pedido, identificador, layout, cnpj, cod_cli, pedido, data, produtos, qtde_itens,qtde_total_unid


for arquivo in arquivos:
    master_formula(arquivo)

print(f'{len(arquivos)} arquivos')
