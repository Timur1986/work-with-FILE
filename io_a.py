# В новый файл добавить текст

new_line = open('wikipedia.txt', 'a')
new_line.write (' The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991.')

new_line.close()
print('Новый текст добавлен!')

# Метод с 'WITH'
'''with open('wikipedia.txt', 'a') as f:
    print(f.write('The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991.'))'''
