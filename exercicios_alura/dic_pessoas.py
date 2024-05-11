pessoas = {'nome':'Alessandra',
           'idade':26,
           'endereco':'Rua xyz',
           'profissao':'aux adm'}
#print(pessoas)

#atualização da idade
pessoas['idade'] = 31

#adicionando raça
pessoas['raça'] = 'Branca'
#print(pessoas)

del pessoas['endereco']
print(pessoas)