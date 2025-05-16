print("Cadastro de Usuário")
usuario_cadastrado = input("Digite o nome de usuário: ")
senha_cadastrada = input("Digite a senha: ")

print("\n--- Login ---")
while True:
    usuario_login = input("Digite seu nome de usuário: ")
    senha_login = input("Digite sua senha: ")
    
    if usuario_login == usuario_cadastrado and senha_login == senha_cadastrada:
        print("Login bem-sucedido! Bem-vindo(a),", usuario_cadastrado)
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.\n")