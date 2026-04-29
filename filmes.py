
#Crie uma lista chamada catalogo com 5 dicionários, cada um representando um filme ou série com as chaves: titulo, nota_avaliacao e ja_assistido.
#Usando um laço for, percorra o catálogo e exiba cada título com a sua classificação (a mesma lógica da Etapa 2).
#Depois, usando um laço while, calcule e exiba a média das notasdo catálogo.



print('----Catálogo de filmes e séries----')
catalogo = [
    {"titulo": "Crepúsculo", "nota_avaliacao": 10.0, "ja_assistido": 'Sim'},
    {"titulo": "Dune", "nota_avaliacao": 8.0, "ja_assistido": 'Sim'},
    {"titulo": "Hawaii 5-0", "nota_avaliacao": 10.0, "ja_assistido": 'Sim'},
    {"titulo": "A empregada", "nota_avaliacao": 10.0,"ja_assistido": 'Sim'},
    {"titulo": "O mentalista", "nota_avaliacao": 9.0,"ja_assistido": 'Sim'}]

for filme in catalogo:
    print(f'Título: {filme['titulo']} - Nota: {filme['nota_avaliacao']} - Já assistido? {filme['ja_assistido']}')

i = 0
soma = 0

while i < len(catalogo):
    soma += catalogo[i]['nota_avaliacao']
    i += 1
print(catalogo[i]['titulo'])
media = soma / len(catalogo)
print(f'Média das notas: {media:.2f}')