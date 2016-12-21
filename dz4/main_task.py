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
    words = ['{}{}'.format(x,y) for x,y in zip(IDs, words1)]
    return words


def text():  #  создает массив с изменяемой частью команд для таблицы Text
    f = open('lukomorie.txt','r',encoding='utf-8')
    a = f.read()
    f.close()
    a = a.replace('\n',' ')
    a = re.sub('(,|\.+|:|;|!|\?)',' \\1',a)
    tokens_raw = a.split(' ')
    tokens = []
    for token in tokens_raw:
        token = '\'' + token + '\'' + ', '
        tokens.append(token)
    IDs1 = list(range(len(tokens)))
    IDs = []
    for id in IDs1:
        id = str(id) + ', '
        IDs.append(id)
    types = []
    for token in tokens:
        if re.match('(,|\.+|:|;|!|\?)', token):
            types.append(str(0) + ', ')
        else:
            types.append(str(1) + ', ')
    token_nums_raw = []
    for id in IDs1:
        id = int(id) + 1
        token_nums_raw.append(id)
    token_nums = []
    for id in token_nums_raw:
        id = str(id)
        token_nums.append(id)
    comms_raw = ['{}{}{}{}'.format(x, y, z, n) for x, y, z, n in zip(IDs, tokens, types, token_nums)]
    return comms_raw

def make_inserts(words,comms_raw):  #  генерирует команды и записывает их в файл
    with open('commands.txt', 'w') as file:
        for comm_raw in comms_raw:
            command = 'INSERT INTO Text (ID,token,type,token_num) VALUES ' + '(' + comm_raw + ')' + ';\n'
            file.write(command)
        for line in words:
            command = 'INSERT INTO Tokens (ID,token,lemma) VALUES ' + '(' + line.lower() + ')' + ';\n'
            file.write(command)


def main():
    make_inserts(get_token_lemma(),text())

if __name__ == '__main__':
    main()

