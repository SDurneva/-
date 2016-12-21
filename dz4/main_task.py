import os
import re


def get_token_lemma():  #  обрабатывает текст майстемом, записывает в массив пары токен-лемма и ID
    text_dir = '/Users/sea_fog/Documents/homework/dz4/lukomorie.txt'
    lemmas_dir = '/Users/sea_fog/Documents/homework/dz4/mystemmed.txt'
    os.system('./mystem -n ' + text_dir + ' ' + lemmas_dir)
    f = open('mystemmed.txt', 'r', encoding='utf-8')
    a = f.readlines()
    f.close()
    words1 = []
    for line in a:
        line = '\'' + line.replace('{', '\', \'').replace('}\n', '\'')
        words1.append(line)
    IDs1 = list(range(len(words1)))
    IDs = []
    for id in IDs1:
        id = str(id) + ', '
        IDs.append(id)
    words = []
    words = ['{}{}'.format(x,y) for x,y in zip(IDs, words1)]
    return words


def make_inserts2(words):  #  генерирует команды для таблицы Tokens и записывает их в файл
    with open('commands.txt','w') as file:
        for line in words:
            command = 'INSERT INTO Tokens (ID,token,lemma) VALUES ' + '(' + line.lower() + ')' + ';\n'
            file.write(command)


def make_inserts1(words):  #  генерирует команды для таблицы Text и записывает их в файл
    f = open('lukomorie.txt','r',encoding='utf-8')
    a = f.read()
    f.close()
    a = a.replace('\n',' ')
    a = re.sub('(,|\.+|:|;|!|\?)',' \\1',a)
    elems = a.split(' ')
    print(elems)
#    IDs1 = list(range(len(elems)))
#    IDs = []
#    for id in IDs1:
#        id = str(id) + ', '
#        IDs.append(id)
#    comms_raw = ['{}{}'.format(x,y) for x,y in zip(IDs, elems)]
#    comms_raw1 = []
#    for comm_raw in comms_raw:
#        comm_raw1 = 'INSERT INTO Text (ID,token,punct_left,punct_right,token_num,token_id)' + '(' + comm_raw
#        comms_raw1.append(comm_raw1)
#    puncts = []
#    for elem in elems:
#        if re.match('(,|\.|:|;|!|\?)',elem)



def main():
    make_inserts2(get_token_lemma())
    make_inserts1(get_token_lemma())

if __name__ == '__main__':
    main()

