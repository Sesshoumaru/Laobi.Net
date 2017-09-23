def get_filtered_words():
    result = []
    with open("filtered_words.txt", encoding='UTF-8') as f:
        for line in f.readlines():
            result.append(line.strip())

    return result


def judge_filtered_word(word, filtered_words: list):
    if filtered_words and filtered_words.count(word) > 0:
        return "Freedom"
    else:
        return "Human Rights"

if __name__ == "__main__":
    filtered_words = get_filtered_words()

    while True:
        word = input('请输入字符串查询是否关键字，输入"exit"退出:')
        if word == 'exit':
            break

        print(judge_filtered_word(word,filtered_words))