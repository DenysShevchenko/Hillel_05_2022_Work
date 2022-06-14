FILENAME = "./lessons_4/classwork/generators/rockyou.txt"
SEARCH_KEYWORD = "admin"


# VAR 1
def read_lines_count_v1():
    results = []
    with open(FILENAME, encoding="utf-8") as file:
        for word in file.readlines():
            if SEARCH_KEYWORD in word:
                results.append(word)
    return results


# VAR 2
def read_lines_count_v2():
    with open(FILENAME, encoding="utf-8") as file:
        return [word for word in file.readlines() if SEARCH_KEYWORD in word]


def read_lines_find_word_generator():
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")
                continue


# print("Lines 1: ", len(read_lines_count_v2()))
# print("Lines 2: ", read_lines_find_word_generator())

for line in read_lines_find_word_generator():
    print(line)
