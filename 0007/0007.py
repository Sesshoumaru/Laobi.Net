import os

# 定义统计单个代码文件的行数函数
def count_file(file_name, directory):
    code_count = 0
    blank_count = 0
    note_count = 0

    real_file_name = os.path.join(directory, file_name)
    with open(real_file_name, 'r',encoding='UTF-8') as f:
        for line in f:
            if line == "" or line.isspace():
                blank_count += 1
            elif line.startswith("#"):
                note_count += 1
            else:
                code_count += 1

    return code_count, blank_count, note_count


def count_directory(path):
    dict_count = {}
    for file in os.listdir(path):
        dict_count[file] = count_file(file, path)

    return dict_count


if __name__ == '__main__':
    dict_count = count_directory("codes")

    print("统计结果：")
    for k, v in dict_count.items():
        print("文件 ", k, ":")
        print("  代码行数：", v[0])
        print("  空行行数：", v[1])
        print("  注释行数：", v[2])
        print("")
