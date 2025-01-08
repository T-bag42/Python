import pymysql.cursors  # Usando a biblioteca PyMySQL

# Conexão com o banco de dados
conexao = pymysql.connect(
    host="localhost",  # Servidor local
    user="root",  # Usuário padrão
    password="",  # Senha (vazia para localhost padrão)
    db="erp",  # Nome do banco de dados
    charset="utf8mb4",  # Permite caracteres especiais (ex: acentos)
    cursorclass=pymysql.cursors.DictCursor  # Retorna resultados como dicionários
)

def logarCadastrar(decisao, resultado):
    """
    Função para logar ou cadastrar um usuário no sistema.
    """
    usuarioExistente = False
    verificado = False
    usuarioMaster = False

    if decisao == 1:  # Caso o usuário queira logar
        nome = input('Digite seu usuário: ')
        senha = input('Digite sua senha: ')

        for linha in resultado:  # Verifica cada registro no banco
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioMaster = linha['nivel'] == 2  # Nível 2 é master
                verificado = True
                break

        if not verificado:
            print('Usuário ou senha não correspondem.')

    elif decisao == 2:  # Caso o usuário queira cadastrar
        print('Faça o cadastro')
        nome = input('Digite seu usuário: ')
        senha = input('Digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome']:
                usuarioExistente = True
                break

        if usuarioExistente:
            print('Usuário já cadastrado.')
        else:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO cadastros(nome, senha, nivel) VALUES (%s, %s, %s)',
                        (nome, senha, 1)  # Nível 1 por padrão
                    )
                    conexao.commit()  # Salva alterações
                print('Usuário cadastrado com sucesso!')
            except Exception as e:
                print('Erro ao inserir os dados:', e)

    return verificado, usuarioMaster

# Loop principal
while True:
    try:
        decisao = int(input('Digite 1 para logar e 2 para cadastrar: '))
        if decisao not in [1, 2]:
            raise ValueError('Opção inválida.')
    except ValueError as ve:
        print('Erro:', ve)
        continue

    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM cadastros")
            resultado = cursor.fetchall()  # Carrega os registros do banco

        # Chama a função para logar ou cadastrar
        verifica, usuarioSupremo = logarCadastrar(decisao, resultado)

        if verifica:
            print('Login realizado com sucesso!')
            if usuarioSupremo:
                print('Bem-vindo, usuário master!')
            else:
                print('Bem-vindo, usuário comum!')
            break  # Sai do loop após login bem-sucedido

    except Exception as e:
        print('Erro ao se conectar ao banco de dados:', e)
