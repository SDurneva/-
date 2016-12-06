import requests
import re
from bs4 import BeautifulSoup
import time
import os
from collections import Counter

start_time = time.time()


def get_texts():  # извлекает со страниц тексты и записывает в отдельные файлы
    links = [link.rstrip('\n') for link in open('links.txt', 'r', encoding='utf-8')]
    classes = ['article__text ', 'paragraph-block__text', 'c-article__text',
               'full-text']
    for link in links:
        r = requests.get(link)
        page_html = r.text
        soup = BeautifulSoup(page_html, 'lxml')
        classes_len = len(classes)
        for i in range(0, classes_len):
            for text in soup.find_all('div', attrs={'class': classes[i]}):
                dir = '/Users/sea_fog/Documents/homework/dz3/texts/'
                if not os.path.exists(dir):
                    os.makedirs(dir)
                with open(dir + 'text' + str(i+1) + '.txt', 'w') as file:
                    for hm in text.find_all(re.compile(r'p')):
                        file.write(hm.text + ' ')


def make_sets():  # преобразовaние текстов в множества слов
    directory = '/Users/sea_fog/Documents/homework/dz3/texts'
    files = os.listdir(directory)
    a = []
    for file in files:
        f = open(directory + '/' + file,'r')
        a.append(f.read())
        f.close()
        sets = []
        ready_texts = []
    for text in a:  # a – массив текстов, text – один из текстов
        text = text.lower()
        a1 = text.split()
        a2 = []
        for word in a1:  # a1 – массив из неочищенных слов одного текста
            word = word.strip(',.!?()—[]«»-–')
            a2.append(word)
            set_text = set()
            ready_text = []
            for item in a2:  # a2 – массив из очищенных слов одного текста
                if item != '':
                    set_text.add(item)
                    ready_text.append(item)
        sets.append(set_text)
        ready_texts.append(ready_text)
    print(ready_texts)
    return sets


def intersecs(sets):  # нахождение пересечения множеств слов и запись в файл
    intersection_texts = sets[0] & sets[1] & sets[2] & sets[3]
    alph = sorted(list(intersection_texts))
    dir = '/Users/sea_fog/Documents/homework/dz3/results/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(dir + 'intersec.txt', 'w') as file:
        for word in alph:
                file.write(word + '\n')


def diff(sets):  # нахождение симметрической разности множеств слов и запись в файл
    diff_texts = sets[0] ^ sets[1] ^ sets[2] ^ sets[3]
    alph = sorted(list(diff_texts))
    dir = '/Users/sea_fog/Documents/homework/dz3/results/'
    with open(dir + 'diff.txt', 'w') as file:
        for word in alph:
            file.write(word + '\n')
    return diff_texts


def filter_words(ready_texts, diff_texts):
    texts = []
    words = []
    dir = '/Users/sea_fog/Documents/homework/dz3/results/'
    for text in ready_texts:
        for word in text:
            texts.append(word)
    for word in texts:
        if word in diff_texts:
            words.append(word)
    frequencies = Counter(words)
    for elem in n:
        if frequencies[elem] < 1:
            del frequencies[elem]
    frequents = set(frequencies)
    for freq in frequents:
        with open(dir + 'frequent.txt', 'w') as file:
                file.write(freq + '\n')


def main():
    get_texts()
    intersecs(make_sets())
    diff(make_sets())
    ready_texts = make_sets()
    filter_words(ready_texts, diff())


    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
