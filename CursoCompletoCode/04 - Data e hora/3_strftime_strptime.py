from datetime import datetime

#metodo strftime - formata a data hora em string
data_hora_atual = datetime.now()
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))
#pega a data hora atual la no datetime cria a variavel com mascara em fromato ptbr e formato en e dps
#chama o metodo strftime para formatar oque vier da data hora atual

#metodo strptime - converte string em data hora
data_hora_str = "2023-10-20 10:20"
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))
#aqui ele pegou aquela data que tava como string e passou como parmetros a string e a mascara que quer usar
#pra converter essa data string em um formato de data hora mesmo