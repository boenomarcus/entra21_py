# Crie uma lista com todas as letras do alfabeto

# Remova as vogais dessa lista e crie uma tupla com elas

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro favorito

# Alfabeto completo
alfabeto = [chr(i) for i in range(ord("a"), ord("z") + 1)]

# Tupla com vogais
vogais = ("a", "e", "i", "o", "u",)

# Removendo vogais da lista do alfabeto
for vogal in vogais:
    i = alfabeto.index(vogal)
    if i != -1:
        alfabeto.pop(i)

# Apresentando consoantes e vogais
print(f"\nConsoantes\n{alfabeto}")
print(f"\nVogais\n{vogais}")

# Cria coleção com nome e idade
nome = "marcus"
conj = set()

# Adiciona consoantes que estão no nome
for letra in alfabeto:
    if letra in nome:
        conj.add(letra)

# Adiciona vogais que estão no nome
for letra in vogais:
    if letra in nome:
        conj.add(letra)

# Adiciona idade ao conjunto
conj.add(26)

# Adiciona livro ao conjunto
conj.add("O Crime do Restaurante Chinês")

# Apresanto conjunto com letras do nome, idade e livro
print(f"\nConjunto de letras, idade e livro\n{conj}\n")

