# Вывести на экран количество символов в файле (with)

with open('Kyrgyzstan.txt', 'r') as f:
    print('Количество символов в файле ' + str(len(f.read())))
