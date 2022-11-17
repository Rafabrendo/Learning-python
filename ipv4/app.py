from classes.calcipv4 import CalcIPv4


calc_ipv4 = CalcIPv4(ip='192.168.0.1', mascara='255.255.255.192')
#prefixo = 24 -> significa que a rede está usando 24bits e ta usando o restante dos bits para hosts

print(calc_ipv4.ip)
print(calc_ipv4.mascara)
print(calc_ipv4.rede)
print(calc_ipv4.broadcast)
print(calc_ipv4.prefixo)
print(calc_ipv4.numero_ips)