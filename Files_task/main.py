alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
answer_words = []
with open("data_from_user.txt", "r", encoding="utf-8") as data_from_user:
    for line in data_from_user:
        counter_list = []
        for _ in alphabet:
            counter_list.append(line.lower().count(_))
            print(counter_list)
        with open("sorted_dictionary.txt", "r", encoding="utf-8") as data_from_dictionary:
            for word in data_from_dictionary:
                counter_list_for_dictionary = []
                for _ in alphabet:
                    counter_list_for_dictionary.append(word.count(_))
                i = 0
                while i in range(26):
                    if counter_list[i] < counter_list_for_dictionary[i]:
                        break
                    i += 1
                if i == 26:
                    answer_words.append(word[:-1])
if len(answer_words) == 0:
    print("NO")
elif len(answer_words) == 1:
    print("YES " + str(answer_words[0].upper()))
else:
    print("YES " + str(answer_words[len(answer_words) - 1]))
