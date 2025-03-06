import random
import string 

def gerar_senha(tamanho):
    if tamanho < 4:
        print("O tamanho mínimo é 4 para incluir todos os tipos de caracteres.")
        return None
    
    letra_maiuscula = random.choice(string.ascii_uppercase)
    letra_minuscula = random.choice(string.ascii_lowercase)
    digito = random.choice(string.digits)
    caractere_especial = random.choice(string.punctuation)

    senha_lista = [letra_maiuscula, letra_minuscula, digito, caractere_especial] 

    if tamanho > 4: 
        todos_caracteres = string.ascii_letters + string.digits + string.punctuation 
        for _ in range(tamanho - 4): 
            senha_lista.append(random.choice(todos_caracteres))

    random.shuffle(senha_lista)

    return ''.join(senha_lista)

try:
    tamanho = int(input("Digite o tamanho desejado para a senha: "))
except ValueError:
    print("Por favor, insira um número inteiro válido.")
    exit()

senha = gerar_senha(tamanho)

if senha:
    print("Senha gerada:", senha)
