count_of_bad_words = 0
if __name__ == '__main__':
    count_of_words_in_dictionary = int(input("Уважаемый пользователь, пожалуйста, введите количество слов в словаре: "))
    print("Далее, пожалуйста, заполните словарь...")
    d = {j: str(input()) for j in range(count_of_words_in_dictionary)}
    petias_task = (str(input("Упражнение Пети: "))).split()
    for _ in petias_task:
        if _ not in d.values():
            count_of_stresses = 0
            for i in _:
                if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "Y":
                    count_of_stresses += 1
            if count_of_stresses != 1:
                count_of_bad_words += 1
    print(count_of_bad_words)
