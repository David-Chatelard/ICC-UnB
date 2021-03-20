snake = input()

for i in range(len(snake)):
    if i == 0:
        print(snake[i].upper(), end = '')
    elif i >= 1 and snake[i-1] == '_':
        print(snake[i].upper(), end = '')
    elif snake[i] == '_':
        print('', end = '')
    else:
        print(snake[i], end = '')
        



