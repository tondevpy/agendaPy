import os

agenda = [{'id': 1, 'nome': 'Everton', 'telefone': '11977908041',
           'email': 'evertonmacieira@icloud.com'}]


def interface():
    print('[1] Cadastrar contato\n[2] Visualizar contatos\n[3] Editar contatos\n[4] Excluir contatos\n[5] sair')


def verificarExistencia(email):
    try:
        for usuario in agenda:
            if email == usuario['email']:
                return True
        return False
                
    except:
        print('Ocorreu um erro inesperado')


def cadastro():
    try:
        nome = input('Informe o nome do contato: ').lower()
        telefone = input('Informe o numero do telefone do contato: ')
        email = input('Informe o email do contato: ').lower()
        if verificarExistencia(email):
            os.system('cls')
            print('Esse usuário já esta cadastrado, cadastre um novo usuário!')
            cadastro()
        else:
            if nome and telefone and email:
                cadastrar = {
                    'id': len(agenda) + 1, 'nome': nome, 'telefone': telefone, 'email': email}
                agenda.append(cadastrar)
                os.system('cls')
                print('Usuário cadastrado com sucesso!')
            else:
                print('Ocorreu um erro inesperado')
    except:
        print('Ocorreu um erro inesperado')


def visualizar():
    for usuario in agenda:
        print(f"\nContato: {usuario['nome']}\nTelefone: {usuario['telefone']}\nEmail: {usuario['email']}\n===================================")



def editar():
    print('usuários cadastrados na agenda')
    visualizar()
    email = input('Informe o email do usuário que deseja editar: ').lower()
    if verificarExistencia(email):
        nome = input('Informe o novo nome: ').lower()
        telefone = input('Informe o novo telefone: ').lower()
        novoEmail = input('Informe o novo email: ').lower()
        if nome and telefone and novoEmail: 
            for usuario in agenda:
                 if usuario['email'] == email:
                        usuario['nome'] = nome
                        usuario['telefone'] = telefone
                        usuario['email'] = novoEmail
                        os.system('cls')
                        print('Usuário editado com sucesso!')       
            
        else:
            os.system('cls')
            print('Favor preencha os campos solicitados para atualizar o usuário!')
            editar()
    else:
        os.system('cls')
        print('O email informado não existe')
        editar()
        


def excluir():
    try:
        visualizar()
        print('Informe o email de contatos para excluir!')
        email = input(': ').lower()
        if email and verificarExistencia(email):
            for usuario in agenda:
                if usuario['email'] == email:
                    agenda.remove(usuario)
                    os.system('cls')
                    print('Usuário removido com sucesso!')
    except Exception as e:
        print(f'ERRO [{e}]')


print('Seja bem vindo a agenda de contatos!')

while True:
    interface()
    decisao = input('Informe a opção desejada: ')

    if decisao == '1':
        os.system('cls')
        cadastro()
    elif decisao == '2':
        os.system('cls')
        visualizar()
    elif decisao == '3':
        os.system('cls')
        editar()
    elif decisao == '4':
        os.system('cls')
        excluir()
    elif decisao == '5':
        os.system('cls')
        print('Programa encerrado com sucesso!')
        break
    else:
        print('Informou uma opção inválida!')

