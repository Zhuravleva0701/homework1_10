import time
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.2)
    print(f'Завершилась запись в файл {file}')


start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
print(f'Время работы программы {end_time - start_time}')

start_time = datetime.now()
first = Thread(target=write_words, args=(10, 'example1.txt'))
second = Thread(target=write_words, args=(30, 'example1.txt'))
third = Thread(target=write_words, args=(200, 'example1.txt'))
fourth = Thread(target=write_words, args=(100, 'example1.txt'))

lst = [first, second, third, fourth]
for i in lst:
    i.start()

for i in lst:
    i.join()
end_time = datetime.now()
print(f'Время работы программы {end_time - start_time}')
