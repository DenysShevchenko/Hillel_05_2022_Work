
FILENAME = "./lessons_4/classwork/generators/rockyou.txt"

while True:
    SEARCH_KEYWORD_user = input("Input search keyword (min 3 symbols): ")
    SEARCH_KEYWORD = SEARCH_KEYWORD_user.replace("\n", "")
    if len(SEARCH_KEYWORD) < 3:
        UserAnser = input("Bad keyword, try againe? (y/n): ")

        if UserAnser == "n":
            break
    else:
        break


def read_lines_find_word_generator():
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")
                continue


if len(SEARCH_KEYWORD) >= 3:
    UserAnser = input("Get search results? (y/n): ")
    if UserAnser == "y":
        results = []
        for line in read_lines_find_word_generator():
            results.append(line)

        print(results)
        print("Keywords found: ", len(results))
else:
    print("Short keyword, search is impossible")
