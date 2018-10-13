# Копировать файл с новым названием (способами без with)

x = input('Укажите имя файла для копирования: ')
y = input('Введите новое имя файла: ')
n_conor = open(x, 'rb')
n_chicken = open(y, 'wb')
n_chicken.write(n_conor.read())

n_conor.close()
n_chicken.close()

print('Файл с новым именем успешно создан!')


