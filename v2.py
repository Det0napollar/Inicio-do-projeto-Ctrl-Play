usuarios = {}

def cadastrar_usuario(usuario, senha):
    if usuario in usuarios:
        return "Usuário já existe!"
    usuarios[usuario] = senha
    return "Cadastro realizado com sucesso!"

def verificar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return "Login bem-sucedido!"
    return "Usuário ou senha incorretos."
