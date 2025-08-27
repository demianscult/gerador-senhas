import secrets
import string

def gerar_senha():
    tamanho = 12

    # Garante pelo menos um caractere de cada tipo
    maiuscula = secrets.choice(string.ascii_uppercase)
    minuscula = secrets.choice(string.ascii_lowercase)
    numero = secrets.choice(string.digits)
    simbolo = secrets.choice(string.punctuation)

    # Preenche o restante da senha
    restantes = tamanho - 4
    todos = string.ascii_letters + string.digits + string.punctuation
    senha_restante = ''.join(secrets.choice(todos) for i in range(restantes))

    # Junta tudo e embaralha
    senha_lista = list(maiuscula + minuscula + numero + simbolo + senha_restante)
    secrets.SystemRandom().shuffle(senha_lista)
    senha_final = ''.join(senha_lista)

    return senha_final

print("Senha gerada:", gerar_senha())
