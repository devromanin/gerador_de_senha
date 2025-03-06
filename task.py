import string
from collections import Counter

nome_arquivo = input("Digite o nome do arquivo de texto: ")

try:

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
except FileNotFoundError: 
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
    exit()

texto = texto.lower()

tabela = str.maketrans('','', string.punctuation)
texto_sem_pontuacao = texto.translate(tabela) 

palavras = texto_sem_pontuacao.split()

contagem = Counter(palavras)

mais_comuns = contagem.most_common(10)

print("As 10 palavras mais frequentes são:")
for palavra, frequencia in mais_comuns:
    print(f"{palavra}: {frequencia}") 
