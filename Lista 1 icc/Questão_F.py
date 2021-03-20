segundos_iniciais = int(input())
horas = segundos_iniciais//3600
segundos_restantes = segundos_iniciais%3600
minutos = segundos_restantes//60
segundos_finais = segundos_restantes%60
print(horas, 'h:', minutos, 'm:', segundos_finais, 's', sep='')
      
      
