'''
Desenvolva um programa cujo objetivo é guardar cada produto que possui um código,
uma descrição, um preço e uma quantidade em estoque. 
Nesse caso, o programa deve criar apenas um único produto de teste, com os campos acima listados. 
Em seguida, o programa pede para que o usuário preencha os dados do produto e, 
ao final, o algoritmo deve imprimir, na tela, os dados recém informados via teclado

'''

produto = {
    'codigo': 0,
    'Descricao':"",
    'preco': 0.0,
    'quantidade': 0.0


}
produto['codico'] = int (input("Digite o codigo do produto:\n"))
produto['Descricao']= (input("Digite a descrição do produto:\n"))
produto['preco']= float (input("Digite o preço sugerido do produto:\n"))
produto['quantidade']= int (input("Digite a quantidade em estoque:\n"))


print ("Codigo: ", produto['codico'])
print ("Descrição: ", produto['Descricao'])
print ("Preço: ", produto['preco'])
print ("Quantidade em estoque: ", produto['quantidade'])


