pessoa = {"nome": "Guilherme", "idade": 28} #igual ao de baixo

pessoa = dict(nome="Guilherme", idade=28) #igual ao de cima modo diferente

pessoa ["telefone"] = "11999999999" #adiciona um novo par chave/valor em um ja criado "pessoa"

#Consulta

pessoa["nome"] #retorna "Guilherme"

pessoa ["idade"] = 29 #altera o valor da chave "idade" para 29

#Retorna : pessoa = {"nome": "Guilherme", "idade": 29, "telefone": "11999999999"}