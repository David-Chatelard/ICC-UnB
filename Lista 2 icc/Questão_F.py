hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()
hora_inicial, minuto_inicial, hora_final, minuto_final = [int(hora_inicial), int(minuto_inicial), int(hora_final), int(minuto_final)]
dh = (hora_final - hora_inicial)
dm = (minuto_final - minuto_inicial)

if dh > 0 and dm > 0:
    print('O jogo durou', dh, 'hora(s) e', dm, 'minuto(s).')
elif dh > 0 and dm < 0:
    print('O jogo durou', dh-1, 'hora(s) e', 60+dm, 'minuto(s).')
elif dh < 0 and dm > 0:
    print('O jogo durou', 24+dh, 'hora(s) e', dm, 'minuto(s).')
elif dh < 0 and dm < 0:
    print('O jogo durou', 23+dh, 'hora(s) e', 60+dm, 'minuto(s).')
elif dh == 0 and dm > 0:
    print('O jogo durou', dh, 'hora(s) e', dm, 'minuto(s).')
elif dh == 0 and dm < 0:
    print('O jogo durou', 23, 'hora(s) e', 60+dm, 'minuto(s).')
elif dh == 0 and dm == 0:
    print('O jogo durou', 24, 'hora(s) e', dm, 'minuto(s).')
elif dh > 0 and dm == 0:
    print('O jogo durou', dh, 'hora(s) e', dm, 'minuto(s).')
elif dh < 0 and dm == 0:
    print('O jogo durou', 24+dh, 'hora(s) e', dm, 'minuto(s).')
    
    

    
