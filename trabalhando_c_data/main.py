# https://docs.python.org/3.0/library/datetime.html
from datetime import datetime, timedelta

#timedelta -> é uma duração

"""
data = datetime(2022, 4, 20, 10, 53, 20)
#year, months, days, hours, minutes, secondes -> hora, minuto e secundo é opcional

print(data) #2022-04-20 10:53:20
#data com o formato padrão Americano

print(data.strftime('%d/%m/%Y')) #20/04/2022
print(data.strftime('%d/%m/%y')) #20/04/22
print(data.strftime('%d-%m-%y')) #20-04-22
#strftime() para formatar uma data
#Eu tenho que colocar directive nos parênteses
print(data.strftime('%d/%m/%Y %H:%M:%S')) #20/04/2022 10:53:20
"""

#Receber uma string contendo uma data, daí se faz o python fazer com que a string vire um objeto data
#parra isso, utilize a função strptime
data = datetime.strptime('20/04/2020', '%d/%m/%Y')
#dai eu converto a string para objeto assim.       # string   ,  formato da data em string

print(data) #2020-04-20 00:00:00
#Formatou no padrão americano e tbm passou a hora, minuto e segundo

#time stemp, é a contagem de segundos desde 1 do 1 da data que mandar
print(data.timestamp())

#fazer uma data por timestamp

data1 = datetime.fromtimestamp(1587351600.0)
print(data1) #2020-04-20 00:00:00

#strptime(str, fmt) -> vai criar um objeto de data a partir de uma string #fmt -> formato(directive)
# .strftime(fmt) ->formata a data
# timestamp ->obter uma time stamp de uma data
# fromtimestamp() -> para obter uma data a partir de um timestamp

data2 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data2 = data2 + timedelta(days=5) #Estou adicionando 5 dias a essa data
print(data2.strftime('%d/%m/%Y %H:%M:%S')) #25/04/1987 20:00:00

data2 = data2 + timedelta(minutes=10, seconds=59) #poderia ter mandado ali, junto com o days
print(data2.strftime('%d/%m/%Y %H:%M:%S'))#25/04/1987 20:10:59


data2 = data2 + timedelta(seconds=2*60*60) #Posso fazer calculos tbm #Nesse caso eu mandei duas
print(data2.strftime('%d/%m/%Y %H:%M:%S')) #25/04/1987 22:10:

#comparando datas
data3 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data4 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')

dif = data4 - data3 #Vou pegar a diferença entre datetima
print(dif) #5 days, 2:33:
print(dif.seconds) #So os segundos #9180 #diferença entre as horas, sem considerar os dias
print(dif.total_seconds()) #segundos totais 441180.0 #5dias e algumas horas e minutos
print(dif.days) #5

print(data3.time())#Eu vou ver só a hora da data #20:00:00

#comparando datas
print(data4 > data3) #True
print(data4 == data3) #False




