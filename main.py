import numpy as np


def readArrFromFile():
    f = open('input.txt', encoding="utf-8")
    array = [line.replace("\n", "")
             for line in f]
    f.close()

    return array


def writeAnswerToFile(array):
    f = open("output.txt", 'w')
    f.write(str(array))


def task(array):
    sentence = array[0]
    roots = array[1:]
    words = [word for word in sentence.split(" ")]

    for k in range(len(words)):  # Проходимся по словам
        word = words[k]  # Берем слово
        for root in roots:  # Проходимся по корням
            if len(word) >= len(root):
                diff = len(word) - len(root)
                for i in range(diff + 1):  # Проходимся по частям слова по длине корня
                    word_root = word[i:len(word) - (diff - i)].lower()
                    root_exc = False  # Булеана, которая проверяет одна ли ошибка в корне слова
                    for j in range(len(word_root)): # проход по взятым буквам слова
                        if word_root[j] != root[j]:
                            if root_exc is True:
                                break
                            else:
                                root_exc = True
                        if root_exc is True and j == len(word_root) - 1: # если взяли дошли до конца взятых букв ка в корне и одна ошибка
                            title = False
                            if words[k].istitle():
                                title = True
                            words[k] = word[:i] + root + word[len(word_root) - i:]
                            if title is True:
                                words[k] = words[k].title()
    return words


if __name__ == '__main__':
    writeAnswerToFile(np.array_str(np.array(task(readArrFromFile())))
                      .replace('[', '').replace(']', '').replace('\'', ''))