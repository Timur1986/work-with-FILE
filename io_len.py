# Вывести на экран количество символов в файле Kyrgyzstan.txt

x = input('Укажите имя файла: ')
Kyrgyz = open(x,'r')
print('В данном файле ' + str(len(Kyrgyz.read())) + ' символов!!!')
Kyrgyz.close()




