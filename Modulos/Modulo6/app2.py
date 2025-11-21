#dicionario tem que ter chaves imutavies mas valores das chaves podem ser mutaveis ou imutaveis
#dicionario troca o nome se passa chave que ja exite com outro nome e chaves que nao tem ele adiciona

contatos = {
    "gui#gmail.com": {
        "nome": "Guilherme",
        "telefone": "3333-2221"
    },
    "lu#gmail.com": {
        "nome": "Luciana",
        "telefone": "3333-4444"
    },
    "ana#gmail.com": {
        "nome": "Ana",
        "telefone": "3333-5555"
    },
    "pedro#gmail.com": {
        "nome": "Pedro",
        "telefone": "3333-6666"
    }
}

telefoneAna = contatos["ana#gmail.com"]["telefone"] #retorna '3333-5555'
print(telefoneAna)


for chave, valor in contatos.items():
    print (chave, valor)

contatos.keys() #retorna todas as chaves do dicionario
contatos.values() #retorna todos os valores do dicionario
contatos.items() #retorna todos os pares chave/valor do dicionario

contatos.get("gui#gmail.com") #retorna o valor da chave "gui#gmail.com"
contatos.get("pedrinho#gmail.com",{}) #retorna o valor da chave "chave" se nao existir retorna um dicionario vazio
contatos.pop("lu#gmail.com") #remove o par chave/valor da chave "lu#gmail.com" e retorna o valor removido

contatos.setdefault("ana#gmail.com", "Juliana") #se a chave "ana#gmail.com" existir retorna o valor dela, se nao existir adiciona a chave com o valor "Juliana"
#retorna : {'nome': 'Ana', 'telefone': '3333-5555'}


"gui#gmail.com" in contatos #retorna True se a chave "gui#gmail.com" existir no dicionario contatos, senao retorna False
"marcos#gmail.com" in contatos #retorna False

del contatos["pedro#gmail.com"] #remove o par chave/valor da chave "pedro#gmail.com"
del contatos["ana#gmail.com"]["telefone"] #remove o par chave/valor da chave "telefone" do dicionario da chave "ana#gmail.com" s