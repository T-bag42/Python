import matplotlib.pyplot as plt
import pymysql.cursors #esta usando uma biblioteca baixada (pymysql)

conexao = pymysql.connect(
	host="localhost", #por estar usando um programa local no PC
	user="root", #usuario padrão do programa
	password="",
	db="erp", #nome do banco de dados criando no SQL
	charset="utf8mb4", #permite usar caraceres com acentos e outras da norma PT-BR
	cursorclass = pymysql.cursors.DictCursor #não sei para que serve!!!!!
)

autentico = False

def logarCadastrar(): #estamos criando um função para facilitar a manutenção
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False



    if decisao == 1: #Caso o usuario queira logar
        nome = input('Digite seu usuario:...')
        senha = input('Digite sua senha:...')

        for linha in resultado: #ele vai verificar se o nome e a senha estão no banco de dados
            if nome == linha['nome'] and senha == linha['senha']: #Verifica se as duas condições são verdadeiras
                if linha['nivel'] == 1: #Está verificando se não tem acesso Master
                    usuarioMaster = False
                elif linha['nivel'] == 2: #Está verificando se tem acesso Master
                    usuarioMaster = True
                autenticado = True 
                break
            else:
                autenticado = False
       
        if not autenticado: # retorna caso não encontre o usuario ou senha no banco de dados a msg a baixo
            print('Usuario ou senha não correspondem')

    




    elif decisao == 2: #Caso o usuario queira cadastrar 
        print('Faça o cadastro')
        nome = input('Digite seu usuario:...')
        senha = input('Digite sua senha:...')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']: #Verifica se já está cadastrado no banco de dados
                usuarioExistente = 1

        if usuarioExistente == 1:
            print('Usuario já cadastrado')
        elif usuarioExistente == 0: #SE usuario ou senha não cadastrados ira cadastrar
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)', 
                                   (nome, senha, 1)
                    ) #usando comandos SQL para cadastrar no BD nome, Senha e nivel sempre com 1
                    conexao.commit()
                print('Usuario cadastrado com sucesso')
            except: #caso não consiga cadastrar
                print('Erro ao inserir os dados')

    return autenticado, usuarioMaster

def cadastrarProdutos():
    produto = input('Digite o nome do produto: ')

    try:
        with conexao.cursor() as cursor: # Verificar se o produto já está cadastrado
            cursor.execute("select nome from produtos where nome = %s", (produto,))
            resultado = cursor.fetchone()  # Busca apenas um resultado

            if resultado:  # Se encontrar um produto com o mesmo nome
                print('Produto já cadastrado!')
                return  # Sai da função, pois o produto já existe
            
            ingredientes = input('Digite os ingredientes do produto: ')
            grupo = input('A qual grupo esse produto pertence: ')
            preco = float(input('Digite o preço do produto: '))

            # Se não existir, cadastra o produto
            cursor.execute(
                'insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)',
                (produto, ingredientes, grupo, preco)
            )
            conexao.commit()  # Confirma a operação no banco de dados
            print('Produto cadastrado com sucesso!')
    except Exception as e:
        print('Erro ao acessar o banco de dados:', e)

def listarProdutos():
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrados = cursor.fetchall()
    except Exception as e:
        print('Erro ao acessar o banco de dados:', e)
    
    for i in produtosCadastrados:
        produtos.append(i)
    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print('Nenhum produto cadastrado')

def excluirProdutos():
    idDeletarPro = int(input('Qual produto deseja excluir...'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDeletarPro))
    except Exception as e:
        print('Erro ao acessar o banco de dados:', e)

def listarUsuarios():
    User = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            userCadastrados = cursor.fetchall()
    except Exception as e:
        print('Erro ao acessar o banco de dados:', e)
    
    for i in userCadastrados:
        User.append(i)
    if len(User) != 0:
        for i in range(0, len(User)):
            print(User[i])
    else:
        print('Nenhum usuario cadastrado')

def excluirUsuarios():
    idDeletarUser = int(input('Qual usuario deseja excluir...'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from cadastros where id = {}'.format(idDeletarUser))
    except Exception as e:
        print('Erro ao acessar o banco de dados:', e)

def teste():
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticavendido')
            produtosCadastrados = cursor.fetchall()
    except Exception as e:
        print('Erro ao acessar o banco de dados:', e)
    
    for i in produtosCadastrados:
        print(i)

def gerarRelatorio():
    nomeProduto = []
    nomeProduto.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()
    except Exception as e:
        print('Erro ao acessar o banco de dados (produtos):', e)
        return

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticavendido')
            vendido = cursor.fetchall()
    except Exception as e:
        print('Erro ao acessar o banco de dados (estatisticavendido):', e)
        return

    estado = int(input('Digite 0 para sair, 1 para pesquisar nome e 2 para pesquisar por grupo... '))

    if estado == 1:
        decisao3 = int(input('Digite 1 para pesquisar por dinheiro ou 2 para qtd unitaria... '))

        if decisao3 == 1:
            for i in produtos:
                nomeProduto.append(i['nome'])

            valores = []
            valores.clear()

            for h in range(len(nomeProduto)):
                somaValor = 0
                for i in vendido:
                    if i['nome'] == nomeProduto[h]:
                        somaValor += i['preco']
                valores.append(somaValor)

            if not nomeProduto or not valores:
                print("Não há dados suficientes para gerar o gráfico.")
                return

            plt.plot(nomeProduto, valores)
            plt.title('Relatório')
            plt.xlabel('Produtos')
            plt.ylabel('Qtd vendida em R$')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif decisao3 == 2:
            grupoUnico = []

            for i in produtos:
                grupoUnico.append(i['grupo'])

            grupoUnico = sorted(set(grupoUnico))

            qtdFinal = []

            for h in range(len(grupoUnico)):
                qtdUnitaria = 0
                for i in vendido:
                    if grupoUnico[h] == i['grupo']:
                        qtdUnitaria += 1
                qtdFinal.append(qtdUnitaria)

            if not grupoUnico or not qtdFinal:
                print("Não há dados suficientes para gerar o gráfico.")
                return

            plt.plot(grupoUnico, qtdFinal)
            plt.title('Relatório')
            plt.xlabel('Grupos')
            plt.ylabel('Qtd Unitaria vendida')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    elif estado == 2:
        decisao3 = int(input('Digite 1 para pesquisar por dinheiro ou 2 para qtd unitaria... '))

        if decisao3 == 1:
            for i in produtos:
                nomeProduto.append(i['grupo'])

            valores = []
            valores.clear()

            for h in range(len(nomeProduto)):
                somaValor = 0
                for i in vendido:
                    if i['grupo'] == nomeProduto[h]:
                        somaValor += i['preco']
                valores.append(somaValor)

            if not nomeProduto or not valores:
                print("Não há dados suficientes para gerar o gráfico.")
                return

            plt.plot(nomeProduto, valores)
            plt.title('Relatório')
            plt.xlabel('Grupos')
            plt.ylabel('Qtd vendida em R$')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif decisao3 == 2:
            grupoUnico = []

            for i in produtos:
                grupoUnico.append(i['grupo'])

            grupoUnico = sorted(set(grupoUnico))

            qtdFinal = []

            for h in range(len(grupoUnico)):
                qtdUnitaria = 0
                for i in vendido:
                    if grupoUnico[h] == i['grupo']:
                        qtdUnitaria += 1
                qtdFinal.append(qtdUnitaria)

            if not grupoUnico or not qtdFinal:
                print("Não há dados suficientes para gerar o gráfico.")
                return

            plt.plot(grupoUnico, qtdFinal)
            plt.title('Relatório')
            plt.xlabel('Grupos')
            plt.ylabel('Qtd Unitaria vendida')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    


while not autentico:

    decisao = int(input('Digite 1 para logar e 2 para cadastrar...'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM cadastros")
            resultado = cursor.fetchall() # Busca os dados retornados pela consulta
            for linha in resultado:  
              print(linha)
    except:
        print('Erro ao se conectar ao banco de dados')

    autentico, usuarioSupremo = logarCadastrar()
    
    if autentico == True:
     print('Usuario autenticado')

if usuarioSupremo == True: # Verificação de usuário master e menu de cadastro

    decisaoUsuario = 1

    while decisaoUsuario != 0:
        decisaoUsuario = int(input('Digite 0 para sair, 1 para cadastrar um produto, 2 para ver produtos cadastrados, 3 para ver usuarios cadastrados ou 4 para visualizar o relatório: '))

        if decisaoUsuario == 1:
            cadastrarProdutos()
        elif decisaoUsuario ==2:
            listarProdutos()

            deleteProd = int(input('Digite 1 para excluir ou 2 para sair'))

            if deleteProd == 1:
                excluirProdutos()

                print('Produto excluido com sucesso')

        elif decisaoUsuario == 3:
            listarUsuarios()

            deleteUser = int(input('Digite 1 para excluir ou 2 para sair'))

            if deleteUser == 1:
                excluirUsuarios()

                print('Usuario excluido com sucesso')

        elif decisaoUsuario == 4:
            gerarRelatorio()

        elif decisaoUsuario == 5:
            teste()
