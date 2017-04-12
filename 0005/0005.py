from collections import Counter
import os


def get_words_perline(file_name):
    """
    获取每行的单词
    :type file_name: 文件名
    """
    lines = []

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            for line in f:
                lines.append(line.split())
    return lines


def get_word_count(file_name):
    """
    统计单词出现次数
    :type file_name: 文件名
    """
    lines = get_words_perline(file_name)
    cnt = Counter()
    for line in lines:
        cnt = cnt + Counter(line)
    print(cnt)


if __name__ == "__main__":
    get_word_count("word.txt")
