#A partir da lista catalogo da Etapa 3, faça o seguinte:
#Adicione um 6º título usando .append()
#Remova o 2º título da lista usando .pop(1)
#Exiba a lista atualizada com os nomes dos títulos
#Exiba quantos títulos o catálogo tem agora, usando len()
#Exiba o título com a maior nota e o com a menor nota


print('----Catálogo de filmes e séries----')
catalogo = [
    {"titulo": "Crepúsculo", "nota_avaliacao": 10.0, "ja_assistido": 'Sim'},
    {"titulo": "Dune", "nota_avaliacao": 7.0, "ja_assistido": 'Sim'},
    {"titulo": "Hawaii 5-0", "nota_avaliacao": 9.0, "ja_assistido": 'Sim'},
    {"titulo": "A empregada", "nota_avaliacao": 8.0,"ja_assistido": 'Sim'},
    {"titulo": "O mentalista", "nota_avaliacao": 8.5,"ja_assistido": 'Sim'}]
catalogo.append({"titulo":'Magnum P.I', 'nota_avaliacao':9.5, "ja_assistido":'Sim'}) #adicionei mais um título
catalogo.pop(1) #removi o segundo título

for filme in catalogo:
    print(f'Título: {filme["titulo"]} - Nota: {filme["nota_avaliacao"]} - Já assistido? {filme["ja_assistido"]}')

print(f'O catálogo possui {len(catalogo)} títulos')

menor=catalogo[0]['nota_avaliacao']
maior=catalogo[0]['nota_avaliacao']

for filme in catalogo:
    nota=filme["nota_avaliacao"]
    titulo=filme["titulo"]

    if nota>maior:
        maior=nota
        titulo=filme["titulo"]

    elif nota<menor:
        menor=nota
        titulo2=filme["titulo"]
    

print(f'O filme com maior avaliação é: {titulo} - nota:{maior};\nO filme com menor avaliação é: {titulo2} - nota:{menor}')

#irá retornar que o filme 'A empregada' é o com menor avaliação, pois removeu o segundo título