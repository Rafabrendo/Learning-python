from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays





#setlocale(LC_ALL, '')
#mandar LC_ALL, e '' vai tentar utilizar o local padrão do computador do usuário
#posso mandar tbm 'pt_BR.utf-8' -> portugues do brasil
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now() #vai pegar a data de agora
formatacao1 = dt.strftime('%A, %d de %B de %Y')
#Obs.: Estou passando os directive
print(formatacao1) #Thursday, 03 de November de 2022  #com o setlocale -> quinta-feira, 03 de novembro de 2022

formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao2) #03/11/2022 16:22:50


mes_autal = int(dt.strftime('%m'))

print(mdays) #[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#Descarta o 0. Começa com o indice 1 que é 31(janeiro)

print(mes_autal, mdays[mes_autal]) #11 30 #apareceu o numero do mes e mostrou quantos dias tem

from calendar import monthrange

# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2020, 2))

# Saída - (5, 29)
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês

from calendar import monthrange
dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)

from datetime import datetime
from calendar import monthrange



"""def monthrange(year, month):
Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
       year, month.
       
       Quando eu chamar o modulo, vai pra essa função no calender e lá vai retornar isso."""

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
# Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Observação: meu ano atual é 2020 neste momento