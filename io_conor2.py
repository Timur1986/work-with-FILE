# Копировать файл с новым названием (способ с with)

x = input('Укажите имя файла для копирования: ')
y = input('Введите новое имя файла: ')

with open(x, 'rb') as f:
    print(f.read)
    with open(y, 'wb') as z:
        print(z.write)
        z.write(f.read())
