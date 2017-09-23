def get_filtered_words():
    result = []
    with open("filtered_words.txt", encoding='UTF-8') as f:
        for line in f.readlines():
            result.append(line.strip())

    return result


def repalce_filtered_word(word:str, filtered_words: list):
    for filtered_word in filtered_words:
        word = word.replace(filtered_word,'*'* len(filtered_word) )
    return word

if __name__ == "__main__":
    filtered_words = get_filtered_words()

    while True:
        word = input('请输入字符串替换关键字，输入"exit"退出:')
        if word == 'exit':
            break

        print(repalce_filtered_word(word,filtered_words))